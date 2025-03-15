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
# encode the categorical data
x = np.arange(100)
WHOREGIONvalues.append(WHOREGIONseries.get(category))

def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return f"{pct:.1f}%\n({absolute:d})"

plt.pie(WHOREGIONvalues, labels=WHOREGIONcategories, autopct=lambda pct: func(pct, WHOREGIONvalues))
```