---
tags:
  - security
  - windows
  - active_directory
aliases:
  - CVE-2022-26923
---
A vulnerability that allows domain users escalate privileges on a [[Windows Active Directory|AD]] domain.
Patched since [[Windows Server 2022]].
# Requirements
- Domain user creates a computer account with permissions:
	- `Validated Write to DNS Host Name`
	- `Validate Write to Service Principal Name`
- User can change DNS host name `dNSHostName` and [[Service Principal Name]]
# Attack
1. Clear all [[Service Principal Name|SPNs]] that include the target's DNS hostname (e.g `DC.DOMAIN.LOCAL`)
2. Change `dNSHostName` to the target's DNS hostname (e.g `DC.DOMAIN.LOCAL`)
3. Request a certificate for the computer account using the `Machine` template. The CA will use the `dNSHostName` value for identification and issue a cert for the domain controller
4. Authenticate as the DC