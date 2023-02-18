###### Variable and Memory
- Identifier names are case-sensitive.
- Must follow certain rules.
- Should follow ceratin conventions.

###### Must
- Start with underscore (_) or letter (a-z A-Z)
- Followed by any number of underscore (_), letters (a-z A-Z), or digits (0-9)
- Exampple of legal name
```
var
my_var
index1
index_1
_var
__var
__lt___
```
- Example of reserved words
```
None
True
False
and
or
not
if
else
elif
for
while
break
continue
pass
def
lambda
global
nonlocal
return
yield
del
in
is
assert
class
try
except
finally
raise
import
from
with
as
```

###### Conventions
- This is a convetion to indicate "internal use" or "private" objects. Object named thisway will not get imported by a statement such as: from module import *
```
_my_var
```
- Used to "mangle" class attributes - useful in inheritance chains
```
__my_var
```
- Used for system-defined names that have a special meaning o the interpreter.
```
__my_var__
```

###### Others convetions
- Packages
    - short, all-lowercase name. Preferably no underscore.
    ```
    utilities
    ```
- Modules
    - short, all-lowercase name. Can have underscores.
    ```
    db_utils
    dbutils
    ```
- Classes
    - CapWords convention
    ```
    BankAccount
    ```
- Functions
    - lowercase, words separated by underscores(snak_case)
    ```
    open_account
    ```
- Variables
    - lowercase, words separated by underscores
    ```
    account_id
    ```
- Constants
    - all-uppercase, words separated by underscores
    ```
    MIN_APR
    ```

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

##### Variable are
##### Memory Management
##### Reference Couting
##### Garbage Collection
##### Dynamic vs Static typing
##### Mutability and Immutability
##### Shared References
##### Variable Equality
##### Everything is Object