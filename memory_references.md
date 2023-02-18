##### Memory References
The variable point to one address hexadecimal. In Python, we can find out the memory addredd referenced  by a variable by using the id() function. THis will return a base-10 number. We can convert this base-10 number to hexadecimal, by using the hex() function.
- Exampe
```
my_var_1 = 10 # my_var_1 references the object at 0x1000
my_var_2 = 'hello' # my_var_2 references the object at 0x1002
```
- Example
```
a = 10
print(hex(id(a)))
```
- Example
```
my_var = 10
print(my_var)
print(id(my_var))
print(hex(id(my_var)))
```