###### For Loop
- Example
```
>>> for i range(5):
>>>     print(5)
0
1
2
3
4
```
- Example
```
>>> for in [1, 2, 3, 4]:
>>>     print(i)
1
2
3
4
```
- Example
```
>>> for c in 'Hello':
>>>     print(c)
h
e
l
l
o
```
- Example
```
for x in ('a', 'b', 'c', 4):
    print(x)
a
b
c
4
```
```
- Example
for i, j in [(1, 2), (3, 4), (5, 6)]:
    print(i, j)
# 1 2
# 3 4
# 5 6
```
- Example
```
for i in range(5):
    if i==3:
        break
    print(i)
# 0
# 1
# 2
```
- Example
```
for i in range(1,8):
    print(i)
    if i % 7 == 0:
        print("multiple of 7 found")
    break
else:
    print('No multiples of 7 in the range')
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# multiple of 7 found
```
- Example
```
for i in range(5):
    print("------------------")
    try:
        10 / (i-3)
    except ZeroDivisionError:
        print('divided by 0')
        continue
    finally:
        print('always run')

    print(i)
```
- Example
```
s = 'hello'

for i in enumarate(len(s)):
    print(i, s[i])
# 0 h
# 1 e
# 2 l
# 3 l
# 4 o
```
