---
tags:
  - python
  - machine_learning
---
This is a python library used to make [[Machine Learning/Transformer]].
# Installation
```
pip install git+https://github.com/redwoodresearch/Easy-Transformer.git
```
# Boilerplate
```python
from easy_transformer import EasyTransformer
reference_gpt2 = EasyTransformer.from_pretrained("gpt2-small", fold_ln=False, center_unembed=False, center_writing_weights=False)
```
