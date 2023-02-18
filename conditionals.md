###### Conditionals
- Example
```
a = 6

if a < 5:
    print('a < 5')
else:
    print('a >= 5')
```
- Example
```
a = 8

if < 5:
    print('a < 5')
else:
    if a < 10:
        print('5 <= a < 10')
    else:
        print('a >= 10')
```
- Example
```
a = 5

if a < 5:
    print('a < 5')
elif a < 10:
    print('5 <= a < 10')
elif a < 15:
    print('10 <= a < 15')
elif a < 20:
    print('15 <= a < 20')
else:
    print('a > 20')
```
- Example
```
b = 'a < 5' if a < 5 else 'a >= 5'
print(b)
```