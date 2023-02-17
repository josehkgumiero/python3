###### Python program
- physical lines of code
    - logical lines of code
        - tokenized
            - End with a physical newline character, end with a logical newline token. Sometimes physical newliners are ignored in order to combine multiple physical line into a sigle logical line of code terminated by a logical newline token. Conversion can be explicit or iplicit.
- Implicit
```
#list 
literals: []

literals: [
    1
    ,2
    ,3
]

literals: [
    1 # comment
    ,2 # comment
    ,3 # comment
]

#tuple 
literals: {}

#dicitonary 
literal: {}

# function arguments / parameters
def my_func(
    a # comment
    ,b # comment
    ,c # comment 
):
    print(a,b,c)
```
- Explicit
    - You can break up statements over multiple lines explicit, by using \(backslash) character. Comments can not be part of a statement, not even a multi-line statement.
```
if a \
    and b \
    and c:
```
- Muli-line string literals
Multi-line string lietrals can be createdusing riple demiliters (' single or " double)
```
''' this is 
a multi-line string'''
""" this is 
a multi-line string"""
```
Be aware that non-visible characters such as newlines, tabs, etc. Are actually part of the string - basically anything you type. You can use scaped characters (eng. \n \t), use string formatting, etc.
A multi-line string is just a regular string.
Multi-line strings are not comments, although they can be used as such especially with special comments called docstring.
```
def my_func():
    a = '''a multi-line string
        that is indented in the second line'''
    return a
print(my_func())
