---
tags:
  - ai_safety
---
[[SHapley Additive exPlanations|SHAP]] for model-agnostic like [[Local Interpretable Model-agnostic Explanations|LIME]], but with shapely value guarantees.
![[KernelSHAP-20260128004912595.webp]]
1. Suppose $x$ composed of 4 features $f_{1}, f_{2}, f_{3}, f_{4}$
2. Take coalition samples by replacing excluded features with a background dataset representing them as a coalition vector (0 and 1)
3. Setup a linear regression problem where each datum is the coalition vector and corresponding ML model output
   ![[KernelSHAP-20260128005107109.webp]]
   Fit an overall model $\hat{y} = \phi_{0} + \phi_{1}f_{1} + \phi_{2}f_{2} + \phi_{3}f_{3} + \phi_{4}f_{4}$ where $\phi_{i}$ is the [[Shapley Values]] for feature $f_{i}$