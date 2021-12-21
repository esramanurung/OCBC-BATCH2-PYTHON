import sys
##Add path to sys

from Path import Person 
from Path.person import display, name

##With default import
print("\n\n> With default import")
print(Person.name)
print(Person.devices)
Person.display('Good Morning !')

##Alternate individual object
print("\n\n> Alternate individual object")
print(name)
display('Good Morning !')

##Import with alternative name
print("\n\n> Import with alternative name")
from Path2.person2 import display2 as new_display, name as new_name
print(new_name)
new_display('Good Morning2 !')

##Dir function
print("\n\n> Dir Function")
print(dir(new_name))

##Executing a Module as a Script
## execute in cmd command inside directory "python Person.py"

##Reload module
print("\n\n> Reload Module")
import car
import importlib

print(car.brands)
importlib.reload(car)
print(car.brands)

##Python Packages
print("\n\n> Python Package")
import Pkg.mod1, Pkg.mod2
print(Pkg.mod1.kitchen_sets)
print(Pkg.mod2.artist_kits)

##Package using individual object
print("\n> Package using individual object")
from Pkg.mod1 import kitchen_sets
print(kitchen_sets)
##Package using alt name
print("\n> Package using alt name")
from Pkg.mod1 import kitchen_sets as ks
print(ks)