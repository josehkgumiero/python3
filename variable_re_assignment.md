#### Variable Re-assignment

- When one variable is created with a name tha point to one address of a integer number like the value 10, after that to  point to other number is simple, the same name stop to point to ten and now point to other address number like 15. In fact the value of the objects never can be changed.

- Example
```
a = 10
print(id(a))
print(type(a))
a = 15
print(id(a))
print(type(a))
b = 15
print(id(a))
print(type(a))
print(hex(id(a))==hex(id(b)))
```