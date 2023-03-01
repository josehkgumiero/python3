from packages import module_1


print(module_1.value)

print(module_1.__file__)
print(module_1.__package__)
#print(module_1.__path__)

print("\n")

from packages import pack1

print(pack1.__file__)
print(pack1.__package__)
print(pack1.__path__)
