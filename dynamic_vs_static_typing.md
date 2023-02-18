##### Dynamic VS Static Typing

Staticaly typed is a way that a variable name point to a address and both have the same type explicited. Programming languages is use the statically typed like Jva, C++ and Swift. So when a variable is created, your type is created too and can not be changed.

Python is dynamic typing, so the variable when is created it references a memory address without a type explicited. So this variable type can be changed to string, or number, or boolean.

- Example
```
a = 'Hello'
type_a = type(a)
print(type(a)) # <class 'str'>
a = 10
type_a = type(a)
print(type(a)) # <class 'int'>
```