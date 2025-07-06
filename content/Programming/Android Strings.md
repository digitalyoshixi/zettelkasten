---
tags:
  - android
---
This is a [[Android Resource Files|Resource File]] that includes all the strings within the app.
`/res/values/strings.xml`
Every ui element in a [[Android Screen Layout|Layout]] should reference its text from here.
# Example `strings.xml`
```xml
<resources>
    <string name="app_name">learners</string>
</resources>
```
# Referencing From `strings.xml`
```xml
<activity
	android:name="@string/app_name">
</activity>
```