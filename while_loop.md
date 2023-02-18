###### While Loop
- Example
```
i = 5

while True:
    print(i)
    if i >= 5:
        break
        print('something')
```
- Example
```
min_length = 2

while True:
    name = input("Please enter your name: ")
    if len(name) >= ming_length and name.isprintable() and name.isalpha():
        break
print("Hello, {0}".format(name))
```
- Example
```
a = 0

while a < 10:
    a += 1
    if a  % 2 == 0:
        continue
    print(a) 
```
- Example
```
l = [1, 2, 3]
val = 10
idx = 0

while idx < len(l):
    if l(idx) == vale:
        break
    idx += 1
else:
    l.append(val)

print(l)
```
```
[1, 2, 3, 10]
```