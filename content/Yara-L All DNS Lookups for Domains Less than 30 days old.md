---
tags:
  - security
  - forensics
---
```json
rule domain_prevalence_whois_30d{

  meta:
    author = "Google Cloud Security"
    description = "Detects DNS events querying domains that have a low rolling max prevalence to a new domain."
    type = “alert”
    tags = “prevalence”
    data_source = "EDR, DNS, Entity Graph"
    severity = “Low”
    priority = “Low”
  
  events:
    $dns.metadata.event_type = "NETWORK_DNS"
    $dns.network.dns.questions.name = $domain

    // derived from events ingested by Chronicle
    $prevalence.graph.metadata.entity_type = "DOMAIN_NAME"
    Sprevalence.graph.metadata.source_type = "DERIVED_CONTEXT”
    $prevalence.graph.entity.hostname = $domain
    $prevalence.graph.entity.domain.prevalence.day_count = 16
    $prevalence.graph.entity.domain.prevalence.day_max = 5
    $prevalence.graph.entity.domain.prevalence.rolling_max <= 3
    $prevalence.graph.entity.domain.prevalence.rolling_max > 0
  
    // Whois domains provided by GCTI Feed
    $whois.graph.entity.domain.name = $domain
    $ahois.graph.metadata.entity_type = “DOMAIN_NAME"
    $uhois.graph.metadata.vendor_name = “WHOIS”
    $whois.graph.metadata.product_name = "WHOISXMLAPI Simple Whois”
    $whois.graph.metadata.source_type = “GLOBAL CONTEXT"
    $whois.graph.entity.domain.creation_time.seconds > 0

    // domain was created in the last 36 days
    2592080 > timestamp.current_seconds() - $whois.graph.entity.domain.creation_time.seconds
  
  match:
    $domain over 1d
  
  outcome:
    $risk_score = max (35)
    $event_count = count_distinct($dns.metadata. id)
    $network_dns_questions_name = array_distinct($dns.network.dns.questions.name)
    $network_dns_answers_data = array_distinct ($dns.network.dns.answers.data)
    
    // added to populate alert graph with additional context
    $principal_ip = array_distinct($dns.principal.ip)
    $target_ip = array_distinct($dns.target.ip)
    $principal_process_pid = array_distinct($dns.principal.process.pid)
    $principal_process_file_full_path = array_distinct($dns.principal.process.file.full_path)
    $principal_process_product_specfic_process_id = array_distinct($dns.principal.process.product_specific_process_1d)
}
```