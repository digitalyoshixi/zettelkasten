---
tags:
  - ctf
---
1. Jacky gave me this url to use: `http://169.254.169.254/latest/meta-data/iam/security-credentials/read-only-s3-role`
2. ![[MagpieCTF2025 The Teeny Disappearance-20250223063411321.webp|717]]
3. setup your `~/.aws/config`
   ![[MagpieCTF2025 The Teeny Disappearance-20250224010650955.webp]]
2. Run this to see if you are connected successfully
   ![[MagpieCTF2025 The Teeny Disappearance-20250223063609415.webp]]
![[MagpieCTF2025 The Teeny Disappearance-20250223063806456.webp]]
1. Do an ls to check what is in here. we ahve a directory
   ![[MagpieCTF2025 The Teeny Disappearance-20250223063734106.webp]]
2. Do another ls to check what is in that directory
   ![[MagpieCTF2025 The Teeny Disappearance-20250223064219175.webp]]
3. Download this one:
   ![[MagpieCTF2025 The Teeny Disappearance-20250223064348635.webp]]
4. The file contents are: `magpieCTF{14m_15_700_345y_70_m355_up}`
