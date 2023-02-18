###### Funtions

- Example
```
def func_1()
    print('running func_1')
```
```
>>> func_1
<function __main__.func_1>

>>>> func_1()
running func_1
```
- Example
```
def func_2(a: int, b: int):
    return a * b
```
```
>>> func_2(2, 3)
6

>>> func_2('a',3)
'aaa'

>>> func_2([1, 2], 3)
[1, 2, 1, 2, 1, 2]
```
- Example
```
def func_6():
    print('running func_6')
```
```
>>> type(func_6)
function
```
- Example
```
def func_7():
    print('running func_7')

func = func_7
```
```
>>> func()
'running func_7'
```
- Example
```
>>> lambda x: x ** 2
<function __main__.<lambda>>
```
```
>>> fn1 = lambda x: x ** 2
>>> fn1(2)
4
```