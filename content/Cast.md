---
tags:
  - blockchain
---
Tool to:
- Send [[Remote Procedure Calls|RPC]] calls
- Send transaction
# Call Function
# Send Transaction
```
cast send <contract_address> \
          "function_name(arg1,arg2)” <arg1> <arg2> \
          --rpc-url <rpc_url> \
          --from <sender_account> \
          --private-key <sender_privkey> \
          --value 0ether \
```
- Gas is calculated automatically, no need to set