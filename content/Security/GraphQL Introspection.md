---
tags:
  - security
---
The setting to allow reading of [[GraphQL Schema]].
# Testing for Introspection
```
{
	"query" : "{__schema{queryType{name}}}"
}
```
Should return with name:query
### Testing for Failed `__schema` detecting regex
Try characters ignored by graphql after `__schema` like:
- `\n`
- ` `
- `,`
```
{
	"query": "query{__schema
	{queryType{name}}}"
}
```
### Testing Introspection on Alternate HTTP Verbs
Additionally test introspection on:
- GET request
- POST request with content-type `x-www-form-urlencoded`
```
GET /graphql?query=query%7B__schema%0A%7BqueryType%7Bname%7D%7D%7D
```
# Full Introspection
### Full
```
#Full introspection query

query IntrospectionQuery {
    __schema {
        queryType {
            name
        }
        mutationType {
            name
        }
        subscriptionType {
            name
        }
        types {
         ...FullType
        }
        directives {
            name
            description
            args {
                ...InputValue
        }
        onOperation  #Often needs to be deleted to run query
        onFragment   #Often needs to be deleted to run query
        onField      #Often needs to be deleted to run query
        }
    }
}

fragment FullType on __Type {
    kind
    name
    description
    fields(includeDeprecated: true) {
        name
        description
        args {
            ...InputValue
        }
        type {
            ...TypeRef
        }
        isDeprecated
        deprecationReason
    }
    inputFields {
        ...InputValue
    }
    interfaces {
        ...TypeRef
    }
    enumValues(includeDeprecated: true) {
        name
        description
        isDeprecated
        deprecationReason
    }
    possibleTypes {
        ...TypeRef
    }
}

fragment InputValue on __InputValue {
    name
    description
    type {
        ...TypeRef
    }
    defaultValue
}

fragment TypeRef on __Type {
    kind
    name
    ofType {
        kind
        name
        ofType {
            kind
            name
            ofType {
                kind
                name
            }
        }
    }
}
```
If it doesnt work try removing:
- onOperation
- onFragment
- onField
### One-Liner Without onOperation, onFragment, onField
```
query IntrospectionQuery {\n    __schema {\n        queryType {\n            name\n        }\n        mutationType {\n            name\n        }\n        subscriptionType {\n            name\n        }\n        types {\n         ...FullType\n        }\n        directives {\n            name\n            description\n            args {\n                ...InputValue\n        }\n        }\n    }\n}\n\nfragment FullType on __Type {\n    kind\n    name\n    description\n    fields(includeDeprecated: true) {\n        name\n        description\n        args {\n            ...InputValue\n        }\n        type {\n            ...TypeRef\n        }\n        isDeprecated\n        deprecationReason\n    }\n    inputFields {\n        ...InputValue\n    }\n    interfaces {\n        ...TypeRef\n    }\n    enumValues(includeDeprecated: true) {\n        name\n        description\n        isDeprecated\n        deprecationReason\n    }\n    possibleTypes {\n        ...TypeRef\n    }\n}\n\nfragment InputValue on __InputValue {\n    name\n    description\n    type {\n        ...TypeRef\n    }\n    defaultValue\n}\n\nfragment TypeRef on __Type {\n    kind\n    name\n    ofType {\n        kind\n        name\n        ofType {\n            kind\n            name\n            ofType {\n                kind\n                name\n            }\n        }\n    }\n}
```
### One-Liner for GET Request
```
GET /api?query=query+IntrospectionQuery+{%0A++++__schema%0A+{%0A++++++++queryType+{%0A++++++++++++name%0A++++++++}%0A++++++++mutationType+{%0A++++++++++++name%0A++++++++}%0A++++++++subscriptionType+{%0A++++++++++++name%0A++++++++}%0A++++++++types+{%0A+++++++++...FullType%0A++++++++}%0A++++++++directives+{%0A++++++++++++name%0A++++++++++++description%0A++++++++++++args+{%0A++++++++++++++++...InputValue%0A++++++++}%0A++++++++}%0A++++}%0A}%0A%0Afragment+FullType+on+__Type+{%0A++++kind%0A++++name%0A++++description%0A++++fields(includeDeprecated:+true)+{%0A++++++++name%0A++++++++description%0A++++++++args+{%0A++++++++++++...InputValue%0A++++++++}%0A++++++++type+{%0A++++++++++++...TypeRef%0A++++++++}%0A++++++++isDeprecated%0A++++++++deprecationReason%0A++++}%0A++++inputFields+{%0A++++++++...InputValue%0A++++}%0A++++interfaces+{%0A++++++++...TypeRef%0A++++}%0A++++enumValues(includeDeprecated:+true)+{%0A++++++++name%0A++++++++description%0A++++++++isDeprecated%0A++++++++deprecationReason%0A++++}%0A++++possibleTypes+{%0A++++++++...TypeRef%0A++++}%0A}%0A%0Afragment+InputValue+on+__InputValue+{%0A++++name%0A++++description%0A++++type+{%0A++++++++...TypeRef%0A++++}%0A++++defaultValue%0A}%0A%0Afragment+TypeRef+on+__Type+{%0A++++kind%0A++++name%0A++++ofType+{%0A++++++++kind%0A++++++++name%0A++++++++ofType+{%0A++++++++++++kind%0A++++++++++++name%0A++++++++++++ofType+{%0A++++++++++++++++kind%0A++++++++++++++++name%0A++++++++++++}%0A++++++++}%0A++++}%0A} HTTP/2
```
# Visualizer Site
https://nathanrandal.com/graphql-visualizer/