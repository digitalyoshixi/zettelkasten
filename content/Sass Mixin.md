---
tags:
  - programming
  - web
---
```css
@mixin myfunc($var1, $background){
	height : 100vh;
	flex-direction : $var1;
	align-items : center;
	background : $background;
}

body{
	@include myfunc(column, blue);
}
```