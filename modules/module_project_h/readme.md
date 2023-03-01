# Import variants
- 
```
# module1.py
import math

# Is math in sys.module? If not, load it and insert ref
# Add symbol math to module1's global namespace refereccing the same object
# If math sybol already exists in module1's namespace, replace reference
# sys.modules -> math <module object>
# module1.globals() -> math <module object>

# those are the same to 'import math as r_math'
# sys.modules -> math <module object>
# module1.globals() -> r_math <module object>

# those are the same to 'from math import sqrt'
# sys.modules -> math <module object>
# module1.globals() -> sqrt <sqrt math.sqrt object>

# Those are the same to 'from math import sqrt as r_sqrt'
# sys.modules -> math <module object>
# module1.globals() -> r_sqrt <math.sqrt object>

# Those are the same to 'from math import *'
# sys.modules -> math <module object>
# module1.globals() -> pi <math.pi object>, sin <math.sin object>
```

# Commoality
- In every case the math module was loaded into memory and referenced in sys.modules
- Running ```from math impot sqrt```
    - did not "partially" load math
    - it only affected what symbols were placed in module''s namespace
- Things may be different with packages, but for simple modules this is behavior.