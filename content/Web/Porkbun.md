---
tags:
  - web
---
This is a [[Domain Name|FQDN]] provider.
# Porkbun Nameservers
```
curitiba.ns.porkbun.com
fortaleza.ns.porkbun.com
maceio.ns.porkbun.com
salvador.ns.porkbun.com
```
# Porkbun DNS Updating Script
```sh
#!/bin/bash

# Your API keys
APIKEY="pk1"
SECRETAPIKEY="sk1"

# Mail configuration
MAIL_ENABLED="true"
MAIL_SERVER="smtp.hostinger.com"
MAIL_PORT="587"
MAIL_FROM="admin@lichtlein.dev"
MAIL_TO="simon@lichtlein.dev"
MAIL_PW_USER="simon@lichtlein.dev"
MAIL_PW="thisisnotmymailpw"

# Define the subdomains you want to update
DOMAINS_TO_SET=(
    "*.lan.lichtlein.dev"
)

# Get the current IP address
IP=$(curl -s https://checkip.amazonaws.com/)

sendMail() {
    if [ "$MAIL_ENABLED" != "true" ]; then
        return
    fi
    OPTIND=1
    subject=""
    text=""
    while getopts "s:t:" flag; do
        case $flag in
        s) subject=${OPTARG} ;;
        t) text=${OPTARG} ;;
        esac
    done

    swaks --from $MAIL_FROM \
        --to $MAIL_TO \
        --server $MAIL_SERVER --port 587 --tls \
        --auth LOGIN --auth-user $MAIL_PW_USER --auth-password $MAIL_PW \
        --header "Subject: [lxc-auth] $subject" \
        --body "$text" >/dev/null 2>&1
}

# Function to parse the sub- and rootdomain
parse_domain() {
    local domain="$1"
    sub_domain=$(echo "$domain" | sed 's/\(.*\)\.[^\.]*\.[^\.]*$/\1/')
    root_domain=$(echo "$domain" | sed 's/.*\.\([^\.]*\.[^\.]*\)$/\1/')
    echo "$sub_domain $root_domain"
}

check_current_A_record() {
    local sub_domain="$1"
    local root_domain="$2"

    url="https://api.porkbun.com/api/json/v3/dns/retrieveByNameType/$root_domain/A/$sub_domain"
    response=$(
        curl -s -X POST "$url" \
            -H "Content-Type: application/json" \
            -d '{
                    "secretapikey":"'"$SECRETAPIKEY"'",
                    "apikey":"'"$APIKEY"'"
                }'
    )
    responsecode=$(echo "$response" | jq -r '.status')
    if [ "$responsecode" != "SUCCESS" ]; then
        sendMail -s "$sub_domain.$root_domain - Error while checking A-record" -t "Error while checking A-record for $sub_domain.$root_domain. Response: $response"
        #exit 1
    fi

    responsecode=$(echo "$response" | jq -r '.records')
    if [ "$responsecode" == "[]" ]; then
        sendMail -s "$sub_domain.$root_domain - No A-record found - creating one..." -t "No A-record found for $sub_domain.$root_domain. We try to create one now."

        url="https://api.porkbun.com/api/json/v3/dns/create/$root_domain"
        response=$(
            curl -s -X POST "$url" \
                -H "Content-Type: application/json" \
                -d '{
                	    "secretapikey":"'"$SECRETAPIKEY"'",
                        "apikey":"'"$APIKEY"'",
                        "name": "'$sub_domain'",
                        "type": "A",
                        "content": "0.0.0.0",
                        "ttl": "600"
                    }'
        )
        id=$(echo "$response" | jq -r '.id')
        id_set_ip="0.0.0.0"
    else
        id=$(echo "$response" | jq -r '.records[0].id')
        id_set_ip=$(echo "$response" | jq -r '.records[0].content')
    fi

    echo "$id" "$id_set_ip"
}

# Loop through each subdomain to update DNS records
for domain in "${DOMAINS_TO_SET[@]}"; do

    result=$(parse_domain "$domain")
    read sub_domain root_domain <<<"$result"
    echo "Checking DNS record for subomdain '$sub_domain' on domain '$root_domain'"

    result=$(check_current_A_record "$sub_domain" "$root_domain")
    read id id_set_ip <<<"$result"
    echo "  the id is '$id' and the current set ip is '$id_set_ip'"

    if [ "$id_set_ip" != "$IP" ]; then
        echo "  updating DNS record"
        url="https://api.porkbun.com/api/json/v3/dns/edit/$root_domain/$id"
        response=$(
            curl -s -X POST "$url" \
                -H "Content-Type: application/json" \
                -d '{
                    "secretapikey": "'"$SECRETAPIKEY"'",
                    "apikey": "'"$APIKEY"'",
                    "name": "'"$sub_domain"'",
                    "type": "A",
                    "content": "'"$IP"'",
                    "ttl": "600"
                }'
        )
        echo "  response: $response"
        sendMail -s "$sub_domain.$root_domain - Updated A-record" -t "The A-record for $sub_domain.$root_domain was updated to $IP with status: $response"
    else
        echo "  no change in IP for - skipping update"
        sendMail -s "$sub_domain.$root_domain - No change in A-record" -t "The A-record for $sub_domain.$root_domain was not updated because the IP is still $IP"
    fi
    echo "  "
done
```
From https://gitlab.com/simonlichtlein/porkbun-dns-updater/-/blob/main/porkbun-dns-updater.sh?ref_type=heads