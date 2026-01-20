---
tags:
  - machine_learning
aliases:
  - MSE
---
Can be used to find the quality of an [[Estimator]].
A popular [[Loss Function]] to measure how wrong a model's predictions are.
# Formula
$$MSE = Var + Bias^{2}$$
# Definition
- For $\theta$  as an unknown parameter
- Suppose $T$ is an [[Estimator]] of $\theta$
- $MSE_{\theta}(T) = E_{\theta}[(T- \theta)^{2}]$
# Alternate Definition
- [[MSE As Dart Boards]]
# MSE Proof
- $MSE[T] = var[T] + (E[T]- \theta)^{2}$
- Note that $V[T-\theta] = E[(T-\theta)^{2}] - E[T-\theta]^{2}$
- $\implies V[T] = MSE[T] - (E[T]- E[\theta])^2$
- $\implies V[T] = MSE[T] - (E[T]- \theta)^{2}$
- $\implies V[T] = MSE[T] - (Bias(T))^{2}$
- $\implies MSE = V[T] + Bias[T]^{2}$
