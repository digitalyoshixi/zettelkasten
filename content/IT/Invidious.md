---
tags:
  - IT
---
A [[Youtube]] frontend for private video streaming.
# Installation (Manual)
https://docs.invidious.io/companion-installation/
1. Install [[Crystal]]
2. `sudo apt install make libssl-dev libxml2-dev libyaml-dev libgmp-dev libreadline-dev postgresql librsvg2-bin libsqlite3-dev zlib1g-dev libpcre3-dev libevent-dev fonts-open-sans npm`
3. `npm install -g deno`
### Creating Invidious User
1. `useradd -m invidious`
2. `su - invidious`
3. `git clone https://github.com/iv-org/invidious`
### Setting up [[PostgreSQL]]
1. `systemctl enable --now postgresql`
2. `sudo -i -u postgres`
3. `psql -c "CREATE USER kemal WITH PASSWORD 'yourpasswordhere';"
4. `createdb -O kemal invidious`
5. `exit`
### Setting up invidious
1. `su - invidious`
2. `cd invidious`
3. `make`
4. Generate two secret keys (HMAC_KEY and invidious_companion_key)
	1. `pwgen 16 1`
	2. `pwgen 16 1`
5. 