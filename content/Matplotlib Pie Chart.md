---
tags:
  - python
  - data_science
---
```python
plt.pie(x, labels=labels)
```
# Pie Chart with percentage
```python
x = np.arange(1000)
def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return f"{pct:.1f}%\n({absolute:d})"

plt.pie(x, labels=y, autopct=lambda pct: func(pct, WHOREGIONvalues))
```