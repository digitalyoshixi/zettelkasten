---
tags:
  - networking
---
Allowing [[GeoIP]] location information in [[Wireshark]]
# Setup
1. Install geoip database https://www.maxmind.com/en/geolite2/signup
2. `Preferences > Name Resolution > Upload Geoip Database`
3. `Preferences > Protocols > IPv4 > Enable GeoIP lookups`
# Filtering
```
ip.geoip.country == "United States"
```

```
ip.geoip.lay > 45
```