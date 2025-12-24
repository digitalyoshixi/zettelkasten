---
tags:
  - programming
  - web
aliases:
  - SCSS
---
![[Sass-20240802035639763.webp|326]]
A [[Cascading Style Sheet|CSS]] pre-processor that allows for:
- Advanced styling techniques
- Variables
- Rules
# Concepts
- [[Sass Syntax]]
- [[Sass Variable]]
- [[Sass Mixin]]
- [[Sass Screen Sizes]]
# Boilerplate
```css
@font-face {
font-family: 'Delius';
src: url("./Delius-Regular.ttf") format('truetype');
font-weight: normal;
font-style: normal;
}
  
@font-face {
font-family: 'Rowdies';
src: url("./Rowdies-Regular.ttf") format('truetype');
font-weight: normal;
font-style: normal;
}

$primaryBtn : rgb(33, 204, 213);
$hoverBtn : rgb(13, 86, 90);
body{
background: lightblue;
font-family: Rowdies;
}

header{
display : flex;
justify-content: center;
width: 20;
padding : 2rem;
position : static;
.leftheader{
}
p{
margin : auto;
}
button{
margin: auto;
background: $primaryBtn;
&:hover {
background : $hoverBtn;
}
}
}
```