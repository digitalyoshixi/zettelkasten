---
tags:
  - security
  - cloud
---
# Viewing Extensions of a VM
```
az vm extension list --resource-group RESOURCEGROUPNAME --vm-name VMNAME -o table
```
# Viewing Extension
```
az vm extension show --resource-group RESOURCEGROUPNAME --vm-name VMNAME --name EXTENSIONNAME --query "settings" -o json
```