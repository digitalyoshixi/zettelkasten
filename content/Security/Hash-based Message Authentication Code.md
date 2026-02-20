---
tags:
  - security
  - cryptography
aliases:
  - HMAC
---
A type of [[Hashing]] algorithm designed to produce [[Message Authentication Code|MAC]].
Allows Separation of message from [[Key|Secret Key]] so that the order of secret key + message doesn't matter.
# Algorithm
$$
\text{HMAC}(K,m) = \text{Hash}( (K' \oplus \text{opad}) || \text{Hash}(K' \oplus \text{ipad}|| m) )
$$
Where:
- $\text{Hash}$ is the [[Hashing|Hash]] function
- $m$ is the message to be authenticated
- $K$ is the secret key
- $K'$ is the block-size secret key defined as:
$$
K' = \begin{cases}
H(K) & \text{if } K \text{ is larger than block size}\\
K & \text{otherwise}
\end{cases}
$$
- $||$ is concatenation
- $\oplus$ is bitwise XOR
- $\text{opad}$ is padding consisting of repeated $\{ \text{0x5c}, \text{0x5c} ,\dots \}$
- $\text{ipad}$ is padding consisting of repeated $\{ \text{0x36}, \text{0x36} ,\dots \}$
# Implementations
- [[HMAC-DRBG]]
- [[HS256]]