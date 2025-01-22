---
tags:
  - java
  - programming
  - webcrawler
---
webcrawler library for java.
[https://www.youtube.com/playlist?list=PL2k4Q1S5CYhHC0PIV5veJKMzLBO8I3ih3](https://www.youtube.com/playlist?list=PL2k4Q1S5CYhHC0PIV5veJKMzLBO8I3ih3) 

# Installation
1. Download jar file. https://jsoup.org/download
2. Put it in the /lib folder [[Java Project Manager]]

# Visiting webpages
```java
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import java.io.IOException;

class Main {
  public static void main(String[] args) throws IOException {
    Document doc = Jsoup.connect("https://en.wikipedia.org/wiki/Economic_entomology").get();
    String title = doc.title();
    System.out.println(title);

  }
}
```
# Downloading Images
```java
Connection.Response resultImageResponse = Jsoup.connect(url).ignoreContentType(true).execute();
FileOutputStream out = (new FileOutputStream(new java.io.File(path)));
out.write(resultImageResponse.bodyAsBytes());  // resultImageResponse.body() is where the image's contents are.
out.close();
```