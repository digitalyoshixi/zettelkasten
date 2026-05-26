---
tags:
  - blockchain
---
Tool to:
- Send [[Remote Procedure Calls|RPC]] calls
- Send transaction
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
# Emulate Function
```
cast call $CONTRACT \
  "function_name(arg1,arg2)" <arg1> <arg2> \
  --from $ACCOUNT \
  --value 5ether \
  --rpc-url $RPC_URL
```
- Emulates transaction
- Does not create a transaction on blockchain
- Should always be used for read-only functions