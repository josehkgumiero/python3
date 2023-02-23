##### Object Mutability

Changing the data inside the object is called modifying the internal state of the object. In this situation, the internal data can be modified, but the address of total object can not be changed. The object that can have the internal changed is called mutable, and the object that can not be changed internally is called immutable.

- Objects immutables
    - numbers
    - strings
    - tuples
    - frozen sets
    - user-defined classes
- Objects mutable
    - lists
    - sets
    - dictionaries
    - user-defined classes

##### Example
```
l = [1, 2, 3]
print(l)
tl = type(l)
print(tl)
il = id(l)
print(il)
l.append(4)
print(l)
il2 = id(l)
print(il2)
print(il==il2)
l2 = [1,2,3]
print(l2)
il3 = id(l2)
print(il3)
print(il==il3)

d = dict(k1= 1, k2='a')
print(d)
id1 = id(d)
print(id1)
d['k3'] = 10.5
print(d)
id2 = id(d)
print(id2)
print(id1==id2)

t = (1, 2)
print(t)
idt = id(t)
print(idt)
t = ([1, 2],[3, 4])
print(t)
idt1 = id(t)
print(idt1)
print(idt == idt1)
```