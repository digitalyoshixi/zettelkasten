---
tags:
  - security
  - ctf
---
Initially, docker compose file will hide the flag as environment variables.
![[THEM?!CTF Best Platform-20260501184658079.webp]]
If we look at `entrypoint.sh`, we will move these respective env variables to different files living on the container
![[THEM?!CTF Best Platform-20260501184739191.webp]]
`robots.txt` shows:
![[THEM?!CTF Best Platform-20260501184858034.webp]]
If we search for other flag parts:
![[THEM?!CTF Best Platform-20260501184923261.webp]]
# Part 2
If we look at dashboard, we see that the flag is going to be set as the sys-token data of a image in the page
![[THEM?!CTF Best Platform-20260501185101373.webp]]
Lets try and get into the dashboard.
The first page we are redirected to is index.php which will have this motion for logging in:
![[THEM?!CTF Best Platform-20260501185217803.webp]]
From SQL creation script, we know there is a admin user
![[THEM?!CTF Best Platform-20260501185248355.webp]]
Ok, anyways lets just register a user account
damian : dasdasada
If we try to log in, we get a OTP area. We dont know where it is being sent, but it is handled by Authenticator.jar

![[THEM?!CTF Best Platform-20260501185829455.webp]]
![[THEM?!CTF Best Platform-20260501185854313.webp]]
Lets unzip the jar and see whats inside
![[THEM?!CTF Best Platform-20260501190009621.webp]]
Decompile the class
```java
public class Authenticator {
   private static final String SECRET_KEY = "5up3r_S3cre7_key";

   public static void main(String[] var0) {
      if (var0.length != 1) {
         System.out.println("Error: Missing username argument.");
      } else {
         System.out.println(generateOTP(var0[0]));
      }
   }

   public static String generateOTP(String var0) {
      String var1 = var0 + "_5up3r_S3cre7_key";
      int var2 = 0;

      for(int var3 = 0; var3 < var1.length(); ++var3) {
         var2 = var2 * 31 + var1.charAt(var3);
      }

      return String.format("%06d", Math.abs(var2) % 1000000);
   }
}
```
Ok, so if we run it we should get the OTP
![[THEM?!CTF Best Platform-20260501190123430.webp]]
![[THEM?!CTF Best Platform-20260501190139557.webp]]
Lets inspect, now we find the corresponding data-sys v alue:
![[THEM?!CTF Best Platform-20260501190256374.webp]]
Part_2/5:C4n_L30_
# Part 1
Ok, now lets try to view the admin/panel.php page:
After we flip the switch on the main page:
![[THEM?!CTF Best Platform-20260501190559994.webp]]
We input:
Username: `admin`
Password: `' OR '1'='1' '`
![[THEM?!CTF Best Platform-20260501190952979.webp]]
`Part_1/5:THEM?!CTF{0nly_Us3r_`
# Part 3
Lets log in as a user again
Hmm, ok, no access
![[THEM?!CTF Best Platform-20260501191300458.webp]]
Search online for what is .htaccess, 
    .htaccess is a configuration file for use on web servers running the Apache Web Server software.
	These .htaccess files can be used to alter the configuration of the Apache Web Server software to enable/disable additional functionality and features that the Apache Web Server software has to offer.
![[THEM?!CTF Best Platform-20260501191639146.webp]]
Ok, well lets look at the .htaccess file we are provided:
![[THEM?!CTF Best Platform-20260501192019759.webp]]
Ok, in dashboard there is a way to upload files, but they only accept image filetypes
![[THEM?!CTF Best Platform-20260501192750556.webp]]
Is there a possibility for [[MIME Sniffing]]?
Also, noticed anti-directory traversal in the widget section
![[THEM?!CTF Best Platform-20260501193108436.webp]]
I tried different [[Percent Encoding|URL Encoding]] to make path traversal work, but it directly gets from the link.
Ok, so lets make widget `uploads/.htaccess`
![[THEM?!CTF Best Platform-20260501193905149.webp]]
`Part_3/5:T0w3r_`
# Part 4
Ok, so either we read `/etc/passwd`, or we find a way to try and log into the user and happen to brute force the password.
The `/etc/passwd` records seem normal so we should see if we can read this file from the website or pop a shell somehow
Initial thoughts: Could we upload something that can cause RCE?
Note that the previous upload field would just check the file extension, if it valid, it saves it locally and writes the path for us, later making current avatar the URL to this uploaded file.
![[THEM?!CTF Best Platform-20260501200236993.webp]]