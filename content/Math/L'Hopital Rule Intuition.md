---
tags:
  - math
  - calculus
---
If you get an indeterminate form when $f,g$ cont at $a$
By [[Linearization]], 
$f(x) \sim f(a) + f'(a)(x-a)$
$g(x) \sim g(a) + g'(a)(x-a)$
hence, $\lim_{ x \to a }\frac{f(x)}{g(x)} = \lim_{ x \to a }\frac{f(a)+f'(a)(x-a)}{g(a)+g'(a)(x-a)}$
$\lim_{ x \to a }\frac{f(x)}{g(x)} = \lim_{ x \to a }\frac{0+f'(a)(x-a)}{0+g'(a)(x-a)}$
$\lim_{ x \to a }\frac{f(x)}{g(x)} = \lim_{ x \to a }\frac{f'(a)}{g'(a)}$
Since f cont at a, $\lim_{ x \to a }f(x)=f(a)$
$$\lim_{ x \to a } \frac{f'(a)}{g'(a)} = \lim_{ x \to a} \frac{f'(x)}{g'(x)}  $$