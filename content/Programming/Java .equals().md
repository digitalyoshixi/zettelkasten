---
tags:
  - strings
---
A method used in [[Java Objects]] and [[Java String]].
Used to check equivalence of:
- All fields
- Class type
```
stringa.equals(stringb)
```
Returns a [[Boolean]]
# Overwritten Equals
Must satisfy the axioms of [[Equivalence]]:
- [[Reflexive|Reflexivity]] : For any non-null object, `x.equals(x)` is true
- [[Symmetric]] : For non-null objects `x.equals(y)` $\Longleftrightarrow$ `y.equals(x)`
- [[Transitive]] : For non-null objects, `x.equals(y)` $\wedge$ `y.equals(z)` $\Longleftrightarrow$ `x.equals(z)`
- [[Consistent]] : For non-null objects, Multiple calls of `x.equals(y)` must return the same output
### Example
```java
// Overriding equals() to compare two Complex objects
    @Override
    public boolean equals(Object o) {

        // If the object is compared with itself then return true  
        if (o == this) {
            return true;
        }

        /* Check if o is an instance of Complex or not
          "null instanceof [type]" also returns false */
        if (!(o instanceof Complex)) {
            return false;
        }
        
        // typecast o to Complex so that we can compare data members 
        Complex c = (Complex) o;
        
        // Compare the data members and return accordingly 
        return Double.compare(re, c.re) == 0
                && Double.compare(im, c.im) == 0;
    }
```
# Other Methods
- [[Java .equalsIgnoreCase()]]
- [[Java .compareTo()]]

