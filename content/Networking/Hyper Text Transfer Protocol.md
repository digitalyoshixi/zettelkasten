---
tags:
  - web
  - application_layer
  - networking
aliases:
  - HTTP
---
Protocol for loading web pages.
Uses non-ephemeral port `tcp/80`.

Our computer wants to access a website. So our computer sends a packet to the web server, the web server responds with a home.htm file that our web browser downloads. The web server’s software has been configured to know that the default web page is the file home.htm. When, our browser downloads this file, our web browser automatically loads it.

Each endpoint application uses this HTTP protocol, more specifically both the web-server application and the web browser application make use of the same HTTP protocol in order to fufill the request and return of a web page.

HTTP was created by Tim Berners-Lee in the early 1990s. Berner birthed HTTP functions to ask for contents of web pages, by giving web browser ability to request files from a server, and allowing the server the ability to return file contents.

  

_The full version of most web addresses(urls)(Uniform Resource Locators) being with the letter http:// or https://_

youve seen HTTP requests before. They are like regular REST API, and that is how they should be used.

Commands like “GET home.htm” are sent by the computer, the web server recieves this HTTP request, then returns a http packet with the HTTP header and data(if there is any). In the case where they do have a home.htm file, the return code is 200 which means OK. This was a good request, inside the packet it also has the data, the segments of the file home.htm. A quick note about HTTP requests: HTTP for get will take a filename argument, if none is given, then the webserver will just have to give a default one. The server returns some data. First, the header, it will have the return code. In our above example. A sucessful return code is 200, but you have also sometimes seen http 404(not found), http 403(forbidden) and so on. So, we got our header and parts of our file back. Its important to note that the webserver didn’t send the entire file back in one packet, no! It will send more packets with more of the file data that we need for home.htm. For these following packets, the segment with the header is omited, because it would be redundant to keep sending the same http header.