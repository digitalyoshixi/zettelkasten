---
tags:
  - android
  - software
aliases:
  - Layout
  - Android Layout
---
# Layout
Describes the appearance of the screen written in [[eXtensive Markup Language|XML]].
# Locations
`/app/res/layout/`
![[Android Screen Layout-20250630152904938.webp]]
# Boilerplate
```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:id="@+id/main"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity"
    android:orientation="vertical"
    >


</LinearLayout>
```