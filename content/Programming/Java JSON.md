---
tags:
  - java
---
# Boilerplate
```java
Context ctx = appcontext.getContext();
InputStream IS;
Resources resources = ctx.getResources();
IS = resources.openRawResource(R.raw.questions2);
// read the string contents and parse into json
BufferedReader BR = new BufferedReader(new InputStreamReader(IS));
StringBuilder SB = new StringBuilder();
String line;
while ((line = BR.readLine()) != null) {
    SB.append(line);
}
BR.close(); // prevent leaks
root = new JSONObject(SB.toString());
```