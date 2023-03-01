# Identifier names
- Are case sensitive.
- Must start with underscore (_) or letter (a-z A-Z)
- Must followed by any number of underscores (_), leters(a-z A-Z), or digits (0-9)
- Can not be reserved words:
    - None, True, False, and, or, not, if, else, elif, for, while, break, continue, pass, def, lambda, global, nonlocal, return, yield, del, i, is, assert, class, try, except, finally, raise, import, from , with, as.

# Conventions
- _my_var
    - this is a convetion to indicate 'internal use" or "private" objects
- __my_var
    - used to mangle class attributes - useful in inheritance chains
- __my_var__
    - used for system-defined names that have a special meaning to the interpreter.

# Other naming convetions
- packages
    - short, all-lowercase names, preferably no underscores;
- modules
    - short, all-lowercase names, can have underscores
- classes
    - CapWords convetion
- functions
    - lowercase, words separated by underscores
- variables
    - lowercase, words separated by underscores
- constants
    - all-upperscase, words separated by underscores