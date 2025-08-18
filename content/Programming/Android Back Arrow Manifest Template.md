---
tags:
  - android
---
Allows any [[Android Intent]] that routes to a different [[Android Screen Activity|Activity]] to have a back arrow to return back to the original activity.
![[Android Back Arrow Manifest Template-20250703130930517.webp]]
```xml
<?xml version="1.0" encoding="utf-8"?>  
<manifest xmlns:android="http://schemas.android.com/apk/res/android"  
    xmlns:tools="http://schemas.android.com/tools">  
  
    <application        android:allowBackup="true"  
        android:dataExtractionRules="@xml/data_extraction_rules"  
        android:fullBackupContent="@xml/backup_rules"  
        android:icon="@mipmap/ic_launcher"  
        android:label="@string/app_name"  
        android:roundIcon="@mipmap/ic_launcher_round"  
        android:supportsRtl="true"  
        android:theme="@style/Theme.Learners"  
        tools:targetApi="31">  
        <activity            android:name=".MainActivity"  
            android:label="@string/app_name"  
            android:exported="true"  
            >  
            <intent-filter>                <action android:name="android.intent.action.MAIN" />  
                <category android:name="android.intent.category.LAUNCHER" />  
            </intent-filter>        </activity>        <activity            android:name=".SettingsActivity"  
            android:label="@string/app_name"  
            android:exported="true"  
            android:parentActivityName=".MainActivity"  
            >  
        </activity>    </application></manifest>
```