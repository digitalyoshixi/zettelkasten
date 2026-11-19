---
tags:
  - security
  - cloud
---
A tool to send [[GraphAPI]] requests.
Works with access tokens from [[seamlesspass]]
# Delete Entra Role
```
roadtx graphrequest "https://graph.microsoft.com/v1.0/roleManagement/directory/roleAssignments?\$filter=principalId+eq+'$USEROBJECTID'" --access-token $ACCESSTOKEN
```
Then, get the role id you want to delete
```
roadtx graphrequest "https://graph.microsoft.com/v1.0/roleManagement/directory/roleAssignments/$ROLEID" -m DELETE --access-token $ACCESSTOKEN
```