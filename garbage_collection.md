##### Garbage Collection

In situation that the python management do not clean as well the object address, this situatio is called Circular References. Circular Rferences is a same references with two objects that have one variable point to other object, so object A has a var_1 that poin to object B that has a var_2 that point to oboject A. The memory leak represent this situation and the Garbage Collector clean up this memory lake. Garbage Collector controll programatically using the gc, by deault it is turned on.
- Example
```
import ctypes
import gc

def ref_count(address):
    return ctypes.c_long.from_address(address).value

def object_by_id(object_id):
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return "Object exists"
    return "Not found"

class A:
    def __init__(self):
        self.b = B(self)
        print('A: self: {0}, b: {1}'.format(hex(id(self)), hex(id(self.b))))

class B:
    def __init__(self,a):
        self.a = a
        print('B: self: {0}, b: {1}'.format(hex(id(self)), hex(id(self.a))))

gc.disable()

my_var = A()

print(hex(id(my_var)))
print(hex(id(my_var.b)))
print(hex(id(my_var.b.a)))

a_id=id(my_var)
b_id=id(my_var.b)

print(ref_count(a_id))
print(ref_count(b_id))

print(object_by_id(a_id))
print(object_by_id(b_id))

print(gc.collect())

print('a id', object_by_id(a_id))
print('b id', object_by_id(b_id))
```
