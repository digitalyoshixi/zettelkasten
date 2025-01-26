---
tags:
  - automation
---
A [[No-SQL]] database that has [[Cloud Service Types|Rapid Elasticity]].
This is a technology created because users need to search for things on your website. Rather than using sql queries, which are slow and heavy, you can use elastic.
A search engine formats data, caches it, then retrieves it. Elastic optimizes the caching portion.

### Indexes

Indexes in elastic search are a logical namespace that points to one or more shards in an elastic cluster. It is where data is stored in the form of documents. These containers for documents are called shards.

Index = database
Type = table
Document = row(json format)
Field = column

  

### Shards

Partition spaces or containers of data. It is an apache luscene instance