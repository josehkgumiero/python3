##### Reference Couting

Python Memory Manager does is counting the how many variables references to one same address.

- Example
```
import sys
a = [1, 2, 3]
print(id(a))
print(sys.getrefcount(a))
```