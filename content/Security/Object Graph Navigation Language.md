---
tags:
  - web
  - security
aliases:
  - OGNL
---
A [[Expression Language]] for getting/setting properties of java objects tied to GUI elements.
- Used by [[Apache Struts]]
Evaluated with `${code}` and `%{code}`

```html
<!DOCTYPE html>
<%@taglib prefix="s" uri="/struts-tags" %>
...
<s:form method="post" action=`**`%{#request.contextPath}/orders/%{id}`**` cssClass="form-horizontal" theme="simple">
<s:hidden name="_method" value="put" />`
ID
`<s:textfield id=`**`"id"`**` name="id" disabled="true" cssClass="form-control"/>`
Client
`<s:textfield id=`**`"clientName"`**` name="clientName" cssClass="form-control"/>`
Amount
`<s:textfield id=`**`"amount"`**` name="amount" cssClass="form-control" />
<s:submit cssClass="btn btn-primary"/>
</s:form>
```