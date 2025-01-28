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
```tex
\begin{align*}
	\text{}\\
	\text{}\\
	\text{}\\
\end{align*}
```
### `indent`
```tex
\indent
```
### [[Augmented Matrix]]
```latex
\left[\begin{array}{cccc|c}
x_{11} & x_{12} & \dots & x_{1n}  & b_{1}\\ \\
\vdots\\
x_{j1} & x_{j2} & \dots & x_{jn}  & b_{j}\\ \\
\vdots\\
x_{k1} & x_{k2} & \dots & x_{kn}  & b_{k}\\ \\
\end{array}\right]
```
### [[Piecewise Functions]]
```latex
\[ f(x) = \begin{cases} 
          0 & x\leq 0 \\
          \frac{100-x}{100} & 0\leq x\leq 100 \\
          0 & 100\leq x 
       \end{cases}
\]
```
