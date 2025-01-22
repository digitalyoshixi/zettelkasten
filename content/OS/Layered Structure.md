Many OS now use this structure. Debugging is now easier since it is splitting the systems through multiple layers. This OS structure is very difficult to design because every larger layer has access to the layers smaller than it. The outermost layer has access to all functionality. For every layer we want to access, we will issue system calls to pass to layers below it. This can be very time heavy when we want to access the very bottom layer from the very top layer.

  

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iv7y_tmp_8171dfb342abe28a.png)