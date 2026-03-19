---
tags:
  - math
  - linux
---
# Installation
1. https://miktex.org/download
# Boilerplate
```tex
\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{dsfont}
\begin{document}

\section{Q1}


\end{document}
```
# Tags
### `begin{align}`
$$
\begin{align*}
	\text{a}\\
	\text{b}\\
	\text{c}\\
\end{align*}
$$
### `indent`
```tex
\indent
```
### [[Matrix]]
$$
\left[\begin{array}{cc}
a & b\\
d & d\\
\end{array}\right]
$$
### [[Augmented Matrix]]
$$
\left[\begin{array}{cc|c}
a & b  & 0\\
\vdots\\
c & d & 0\\
\end{array}\right]
$$
### [[Vector]]
$$
\left[\begin{array}{ccc}
a_{11} & \dots & a_{1n} \\
\vdots\\
a_{k1} & \dots & a_{kn} \\
\end{array}\right]
$$
### [[Piecewise Functions]]/System Of Equations
$$
f(x) = \begin{cases} 
          0 & x\leq 0 \\
          0 & x > 0
       \end{cases}
$$

### Embed Images
```latex
\usepackage{graphicx}

\begin{document}

\includegraphics[width=\linewidth]{"./q1.png"}

\end{document}
```