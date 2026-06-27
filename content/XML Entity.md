---
tags:
  - web
  - programming
---
A variable for [[eXtensive Markup Language|XML]] documents that allows usage in other parts of the program defined in the [[Document Type Definition|DTD]]
# General Entity
Entities that can be used anywhere in the document
### Defining
```xml
<?xml version="1.0"?>
<!DOCTYPE Person [
	<!ENTITY name "John">
]>
<Person>
	<Name>&name;</Name>
	<Age>20</Age>
</Person>
```
# Parameter Entity
An entity only allows within the [[Document Type Definition|DTD]] (entitiys that have values of other entities)
```xml
<!ENTITY % outer "<!ENTITY inner 'John'>">
```
# Predefined Entity
Entities that already exist and can be used
```xml
<!--special character x3c-->
<hello>&#x3c;<hello>
```