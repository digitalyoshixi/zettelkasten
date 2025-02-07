---
tags:
  - binary_exploitation
  - security
---
You can brute force a stack canary by forking the process and trying new stack canaries.
This works because every stack canary is only generated **once** for the **parent** process.
In android, the parent process is the [[Zygote Process]]
```c
int main()
	char buf[16];
	while (1){
		if (fork()){
			wait(0);
		}
		else{
			read(0, buf, 128)
			return;
		}
	}
```
![[Stack Canary Brute Forcing-20250207194936768.webp]]
You could check this byte-by-byte until you get the full stack canary discovered