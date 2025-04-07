---
tags:
  - database
---
# Wide Column Database
A key-value database used for long-term storage.
There is key space and column family.
![[Wide Column Database-20241027175137581.webp]]
It is able to handle unstructured data.
You must navigate these using [[Cassandra Query Language|CQL]].
### Pros
- [[Horizontal Scaling]]
- Time-series
- Historical records
- High write, low read

### Implementations
- [[Cassandra]]
- [[HBase]]