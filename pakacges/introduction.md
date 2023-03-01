# Packages
- what is a package?
- why uset them?
- how is it different from a odue?
- the role of __init___.py files in package

# Implicit Namespace Packages
- WHat are they?
- How do we reate and use them?
- Standard packages

# Packages are Modules
- Packages are modules, but modules are not necessarily packages.
- They contain modules, and packages that called sub-packages
- If a module is a package, it must have a value set for __path__
- After  have imported a module, you can easily see if thaat module is a package by inspecting the __path attribute (when it is empty is a module, or when is non-empty it is a package.)

# FIle system
- Remember that modules do not have to be entities in a file system.
- By the same token, packages do not have to be entities in the file system.
- Typically they are modules are file system entities.
- Packages represent a hierarchy of modules/package.
- Dotted notation indicates the path hieararchyof modules / packges and is usually found in __path__
    - 
    ```
    pack1.mod1
    pack1.pack1_1.mod1_1
    ```

# Importing Nested Packages
- If you have a statement in your top-level program such as:
```
import pack1.pack1_1.module1
```

- The import system will perform these steps:
```
imports pack1
imports pack1.pack1_1
imports pack1.pack1_1.module1
```

- The sys.modules cache will contain entries for:
    - pack1
    - pack1.pack1_1
    -pack1.pack1_1.module1

- The namespace where the import was un contains: pack1

# File System Based Packages
- Although modules and packages can be for more generic than file system based entities, it gets complicated!
- If you are interested in this, then the first document you should read is PEP302.
- In this course we are going to stick to traditional file based modules and packages.

# File Based Packages
- Packages paths are created by using file system directories and files.
- On a file system we therefore have to use directories for packages.
- The directory name becomes the package name.
- So where does the code go for the package (since it is a module)? __init__.py

# __init__.py
- TO define a package in our file system, we must:
    - create a directory whose name willl be the package name
    - create a file called __init__.py inside that directory

- that __init__.py file is what tell python tha t the directory is a package as opposed to a standarrd directory.
    - if we do not have an __init__.pyfile, then python creates an implicit namespace package.

# WHat happens when a file based package is imported?
```
app/
    pack1/
        __init__.py
        module1.py
        module2.py
import pack1
```
- the code for pack is in __init__.py
- that code is loaded, executed and cached in sys.modules with a key of pack1
- the symbol pack1 is added to our namespace referecing the same object
- but, it has a __path__ property (file system directory path (absolute))
- also has a __file__ property (file system path to __init__.py (absolute))

# Nested Packages
- Package can contain odules as well as packages
```
app/
    module.py
    pack1/
        __init__.py
        module1a.py
        module1b.py

        pack1_1/
            __init__.py
            module1_1a.py
            module1_1b.py
```
- module inside pack1 - pack1.module1a
- package inside pack1 - pack1.pack1_1
- module inside pack1.pck1_1 - pack1.pack1_1.module1_1b


# __file__, __path__, __package__ Properties
- modules have __file__ and __package__ properties
- __file__ is the location of odule code in the file system
- __package__ is the package the odule code is located in (an empty string if the module is located in the application root)
- if the module is also a package, then it also has a __path__ property
    - __path__ is the location of the package in he file system
```
module.__file__ -> ../app/module.py
module.__path__ -> not set
module.__package__ -> ''

pack1.__file__ -> ../app/pack1/__init__.py
pack1.__path__ -> ../app/pack1
pack1.__package__ -> pack1

pack1.module1a.__file__ -> ../app/pack1/module1a.py
pack1.module1a.__path__ -> not set
pack1.module1a.__package__ -> pack1