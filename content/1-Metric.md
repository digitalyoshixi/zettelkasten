---
tags:
  - math
  - linalg
aliases:
  - Taxi Metric
  - Manhattan Metric
---
# Definition
- Let $x,y \in \mathbb{F}^{n}$
- Let $d(x,y)$ be a [[Metric]] for $\mathbb{F}$
- Let $f(x,y) = \sum_{i=1}^{n} d(x_{i},y_{i})$
- Then, $f$ is a metric for $\mathbb{F}^{n}$
# Proof
### $f(x,y) \geq 0$
- As $d(x_{i}, y_{i}) \geq 0$
- Then, $\forall i, \sum_{i=1}^{n}d(x_{i},y_{i}) \geq 0$
- Then, $\forall i, f(x,y) \geq 0$
### $f(x,y) = f(y,x)$
- Let $x,y \in \mathbb{F}^{n}$
- Then, $x = (x_{1},\dots,x_{n})$
- And $y = (y_{1},\dots,y_{n})$
- $f(x,y) = \sum_{i=1}^{n}d (x_{i},y_{i})$ by defn of $f$
- $= \sum_{i=1}^{n} d(y_{i}, x_{i})$ as $d$ is a metric
- $= f(y,x)$ by defn of $f$
### $f(x,y) = 0 \Longleftrightarrow x=y$
- $f(x,y) = 0$
- $\Longleftrightarrow \sum_{i=1}^{n} d(x_{i},y_{i}) = 0$
- $\Longleftrightarrow d(x_{i},y_{i}) = 0$
- $\Longleftrightarrow x_{i} = y_{i} \forall i$
- $\Longleftrightarrow x = y$
### $f(x,z) \leq f(x,y) + f(y,z)$
- Let $x,y,z \in \mathbb{F}^{n}$
- Then, $x = (x_{1},\dots,x_{n})$
- Then, $y = (y_{1},\dots,y_{n})$
- Then, $z = (z_{1},\dots,z_{n})$
- $f(x,z) = \sum_{i=1}^{n} d(x_{i}, z_{i})$
- $\leq \sum_{i=1}^{n} [ d(x_{i}, y_{i}) + d(y_{i}, z_{i}])$ as $d$ is a [[Metric]]
- $= \sum_{i=1}^{n} d(x_{i}, y_{i}) + \sum_{i=1}^{n} d(y_{i}, z_{i})$
- $= f(x,y) + f(y,z)$