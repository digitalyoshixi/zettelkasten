---
tags:
  - security
  - cryptography
---
A method for multiple people to sign the same message, thus consuming less data on the [[Blockchain]].
# Method
![[Schnorr's Signature-20260529013727297.webp]]
# Creating Signature (1 Person)
- Calculate random nonce $r$
- Calculate public key $R = rG$
- Calculate challenge $e = H(R||A||m)$ where $H$ is a hash fn, $||$ is concatenation
- Construct signature as $s = r+\alpha e$
- Publish $(s,R)$
# Verifying Signature (1 Person)
Verify:
- Calculate $c = sG$
- $e = H(R||A||m)$
- $d = R+Ae$
- If $c=d$, signature is valid
# Creating Signature (Multiple Person)
1. Alice public key $A$, Bob public key $B$
2. Added together $P_{AB} = A+B$
3. Alice picks nonce $r_{A}$ and creates public key $R_{A} = r_{A}G$
4. Bob picks nonce $r_{B}$ and creates public key $R_{B} = r_{B}G$
5. Public keys are added together to create aggregate $R_{AB} =R_{A} + R_{B}$
6. Calculate same challenge $e = H(R_{AB}||P_{AB}|m)$
7. Alice signature $s_{A}=r_{A}+\alpha e$
8. Bob signature $s_{B}=r_{B}+\beta e$
9. Aggregate signature $s_{AB}=s_{A}+s_{B}$
10. Signature published as $(s_{AB},R_{AB})$
# Verifying Signature (Multiple Person)
1. Calculate $c = s_{AB}G$
2. Calculate $e = H(R_{AB}||P_{AB}||m)$
3. Calculate $d=R_{AB}+P_{AB}e$
4. If $c = d$ signature is *valid*