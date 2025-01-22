---
tags:
  - proofs
  - math
---
# Fermat's Theorem
- f'(c) exists
- local max/min at f(c)
Then, $f'(c) = 0$

# Proof
1. Assume $f'(c)$ exists
	1. Suppose $f(c)$ is a local minima
		1. Then, by definition of local minima, $\exists \delta > 0$ s.t $0 < |x - c|< \delta \implies f(x) \geq f(c)$
		2. Let $\delta$ be arbitrary
		3. Suppose $0 < | x - c | < \delta$
		4. Then $f(x) \geq f(c)$
		5. This means $f(x) - f(c) \geq 0$
		6. Since $f'(c)$ exists, then this means that $f(c)$ is continuous. Thus, $\lim_{ x \to c^-} \frac{f(x)-f(c)}{x-c} = \lim_{ x \to c} \frac{f(x)-f(c)}{x-c} = \lim_{ x \to c^+} \frac{f(x)-f(c)}{x-c}$
		8. Then, consider $\lim_{ x \to c^-} \frac{f(x)-f(c)}{x-c}$
			1. $\lim_{ x \to c^- }(x-c) < 0$ as $x\to c^-$
			2. Thus, $\lim_{ x \to c^-} \frac{f(x)-f(c)}{x-c} \leq 0$
		9. Then, consider $\lim_{ x \to c^+} \frac{f(x)-f(c)}{x-c}$
			1. $\lim_{ x \to c^+ }(x-c) > 0$ as $x\to c^+$
			2. Thus, $\lim_{ x \to c^+} \frac{f(x)-f(c)}{x-c} \geq 0$
		10. $0\geq\lim_{ x \to c^-} \frac{f(x)-f(c)}{x-c} = \lim_{ x \to c} \frac{f(x)-f(c)}{x-c} = \lim_{ x \to c^+} \frac{f(x)-f(c)}{x-c}\geq 0$
		11. Thus, $\lim_{ x \to c} \frac{f(x)-f(c)}{x-c}=0$
		12. Thus, $f'(c)=0$
	2. Suppose $f(c)$ is a local maxima
		1. Then, by definition of local maxima, $\exists \delta > 0$ s.t $0 < |x - c|< \delta \implies f(x) \leq f(c)$
		2. Let $\delta$ be arbitrary
		3. Suppose $0 < | x - c | < \delta$
		4. Then $f(x) \leq f(c)$
		5. This means $f(x) - f(c) \leq 0$
		6. Since $f'(c)$ exists, then this means that $f(c)$ is continuous. Thus, $\lim_{ x \to c^-} \frac{f(x)-f(c)}{x-c} = \lim_{ x \to c} \frac{f(x)-f(c)}{x-c} = \lim_{ x \to c^+} \frac{f(x)-f(c)}{x-c}$
		8. Then, consider $\lim_{ x \to c^-} \frac{f(x)-f(c)}{x-c}$
			1. $\lim_{ x \to c^- }(x-c) < 0$ as $x\to c^-$
			2. Thus, $\lim_{ x \to c^-} \frac{f(x)-f(c)}{x-c} \geq 0$
		9. Then, consider $\lim_{ x \to c^+} \frac{f(x)-f(c)}{x-c}$
			1. $\lim_{ x \to c^+ }(x-c) > 0$ as $x\to c^+$
			2. Thus, $\lim_{ x \to c^+} \frac{f(x)-f(c)}{x-c} \leq 0$
		10. $0\leq\lim_{ x \to c^-} \frac{f(x)-f(c)}{x-c} = \lim_{ x \to c} \frac{f(x)-f(c)}{x-c} = \lim_{ x \to c^+} \frac{f(x)-f(c)}{x-c}\leq 0$
		11. Thus, $\lim_{ x \to c} \frac{f(x)-f(c)}{x-c}=0$
		12. Thus, $f'(c)=0$