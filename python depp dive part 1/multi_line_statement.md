# Python program
- physical lines of code
    - logical lines of code
        - tokenized
- End with a physical newline character, end wit a logical newline token.

# Physical newline VS Logical newline
- sometimes, physical newlines are ignored in order to combine mutiple physical lines into a single logical line of code terminated by a logical newline token.

# Implicit conversion
- Expressions in:
    - list literals: []
    - tuple literals; ()
    - dictionary literals: {}
    - set literals: {}
    - function arguments / parameters

# Explicit
- You can break up statements over multiple lines explicit, by using the \ (backslash character)

# Multi-line string literals
- Multi-line string literals can be created using triple delimiters (', or "")
```
'''
This is a multiline string
'''

"""
This is a multi-line string
"""
```
- Be aware that non-visible characters such as newlines, tabs, etc. Are actually part of the string - basically anything you type.
- You can use escaped characters, use tring formattig etc.
- Multi-line trings are not comments, although they can be used as such, especially with special comments called docstrings.