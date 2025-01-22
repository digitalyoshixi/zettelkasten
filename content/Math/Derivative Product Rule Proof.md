---
tags:
  - math
---
If we let p(x) = f(x)g(x)
then using the limit definition, we do:
$$p'(x) = \lim_{h \to 0} [\frac{f(x+h)g(x+h) - f(x)g(x)}{h}]$$
$$p'(x) = \lim_{ h \to 0 } [\frac{f(x+h)g(x+h) - f(x)g(x+h) + f(x)g(x+h) - f(x)g(x)}{h}]$$
$$p'(x) = \lim_{ h \to 0 } [\frac{f(x+h) - f(x)}{h}g(x)+f(x)\frac{g(h+x)-g(x)}{h}]$$
$$p'(x) = \lim_{ h \to 0 } \frac{f(x+h) - f(x)}{h}\lim_{ h \to 0 }g(x)+\lim_{ h \to 0 }f(x)\lim_{ h \to 0 }\frac{g(h+x)-g(x)}{h}$$
$$p'(x) = f'(x)g(x) + g'(x)f(x)$$



