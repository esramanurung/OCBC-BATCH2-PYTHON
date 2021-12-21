##Example of Function Creation

from typing import SupportsBytes


def my_function(p, l):
    '''Function to calculate area of a square'''
    print(p * l)
   
   
def printme( str_input ):
   '''This prints a passed string into this function'''
   print(str_input)


# Tambahan
my_function(9,2)
print(my_function.__doc__)

printme(100)
print(printme.__doc__)

printme("I'm first call to user defined function...")
printme("Again second call to the same function...")



## Calling a Function
# Function definition is here
def printme( str_input ):
   '''This prints a passed string into this function'''
   print(str_input)

# Now you can call printme function
printme("I'm first call to user defined function!")
printme("Again second call to the same function")

##Pass by reference vs value
# Function definition is here
def changeme( mylist ):
   '''This changes a passed list into this function'''
   mylist = mylist+[1,2,3,4]
   print("\nValues inside the function : ", mylist)
   return mylist

# Now you can call changeme function
mylist = [10,20,30]
print("\nValues outside the function - before : ", mylist)
mylist = changeme( mylist )
print("\nValues outside the function - after  : ", mylist)

## being overwritten inside the called function.
# Function definition is here
def changeme( mylist ):
   '''This changes a passed list into this function'''
   mylist = [1, 2, 3, 4] # This would assign new reference in mylist
   print("Values inside the function  : ", mylist)

# Now you can call changeme function
mylist = [10, 20, 30]
changeme( mylist )
print("Values outside the function : ", mylist)

# Tambahan
def save_data(name, age):
    print(f"Nama : {name}")
    print(f"Age + 10 = {age + 10}")
    # return none

save_data('Adi',20)
          #name,age

#tambahan keyword arguments
save_data(age = 20, name= "Adi")


##Tambahan Default arguments
# Function definition is here
def printinfo( name, age = 26 ):   
    "This prints a passed info into this function"   
    print("Name: ", name)   
    print("Age: ", age)   
    return;
# Now you can call 
printinfo( age=50, name="hacktiv8" )
printinfo( name="hacktiv" )

#Function Arguments
# Function definition is here
def printme( str_input ):
   '''This prints a passed string into this function'''
   print(str_input)
 
# Now you can call printme function
printme("Hello")

# # This syntax will give you an error
# printme()

# One more example of required arguments. Let's create function that can calculate area of rectangle.
# Function definition is here
def calculate_rect(length, width):
  '''This function is used to calculate area of rectangle'''
  print('Area : ', length*width)

# Define parameters
length = 100
width = 20

# Call calculate_rect
calculate_rect(length, width)

# # This syntax will give you an error
# calculate_rect(length)

# Keyword Arguments
# Function definition is here
def printme( str_input ):
   '''This prints a passed string into this function'''
   print(str_input)

# Now you can call printme function
printme(str_input = "Hacktiv8")

## The following example gives more clear picture. Note that the order of parameters does not matter.
# Function definition is here
def printinfo( name, age ):
   '''This prints a passed info into this function'''
   print("Name : ", name)
   print("Age. : ", age)

# Now you can call printinfo function
printinfo( age=4, name="a" )

## Default Arguments
# Function definition is here
def printinfo( name, age = 26 ):
   '''This prints a passed info into this function'''
   print("Name : ", name)
   print("Age  : ", age)
   print("")

# Now you can call printinfo function
printinfo( age=50, name="hacktiv8" )
printinfo( name="hacktiv" )

# You must write default-arguments after required-argument
# Function definition is here
def printinfo( name, age = 26 ):
   '''This prints a passed info into this function'''
   print("Name : ", name)
   print("Age  : ", age)
   print("")

# Now you can call printinfo function
printinfo( age=50, name="hacktiv8" )

## Variable-length Arguments
# Function definition is here
def printinfo( arg1, *vartuple ):
# def printinfo(arg1, arg2, arg3, arg4):
   '''This prints a variable passed arguments'''
   print('arg1     : ', arg1)
   print('vartuple : ', vartuple)
   print('')
   
   for var in vartuple:
      print('isi vartuple : ', var) 

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50, "a")
printinfo (70, 60, "a")

##tambahan
penjumlahan = lambda num1, num2, num3 : num1 + num2 + num3
print(penjumlahan(1,2,3))

penjumlahan_copy = penjumlahan(1,2,3)
print(f"copy of penjumlahan = {penjumlahan_copy}")


## Tambahan
def penjumlahan_pengurang(num1, num2):
    sum = num1 + num2
    subt = num1 - num2 

    print(f"subt = {subt}")
    print(f"num1 = {num1}")
    return num1 + num2, num1 - num2
    #return sum, subt

print(penjumlahan_pengurang(10,1))


# Create a function with nonkeyword variables

def person_car(total_data, **kwargs):
  '''Create a function to print who owns what car'''
  print('Total Data : ', total_data)
  for key, value in kwargs.items():
    print('Person : ', key)
    print('Car    : ', value)
    print('')

person_car(3, jimmy='chevrolet', frank='ford', tina='honda')
person_car(3)

# Parameters (jimmy='chevrolet', frank='ford', tina='honda') will be equal to
# kwargs = {
#     'jimmy': 'chevrolet', pkg.mod2.artist_kits
#     'frank': 'ford',
#     'tina': 'honda'
# }

## The Anonymous Functions
# Function definition is here
sum = lambda arg1, arg2: arg1 + arg2

# That lambda function will be equal to :
# def sum(arg1, arg2):
#     return arg1+arg2

# Now you can call sum as a function
print("Value of total : ", sum( 10, 20 ))
print("Value of total : ", sum( 20, 20 ))

## The return Statement
# Function definition is here
def sum(arg1, arg2):
    # Add both the parameters and return them."
    total = arg1 + arg2
    return total

# Now you can call sum function
total = sum(10, 20)
print("Result function : ", total)

## Scope of Variables
# Declare a global variable
total = 0

# Create sum function
def sum( arg1, arg2 ):
   total = arg1 + arg2; 
   print("Inside the function local total   : ", total)

# Call a function
sum( 10, 20 )
print("Outside the function global total : ", total)

# Declare a global variable
total = 0

# Create sum function
def sum( arg1, arg2 ):
   total = arg1 + arg2; 
   print("Inside the function local total   : ", total)
   return total

# Call a function
print("Outside the function global total - before : ", total)
total = sum( 10, 20 )
print("Outside the function global total - after  : ", total)

## Docstring
# Example of docstring in a function

def sum_number(num1, num2):
  '''
  This function is used to sum of 2 variables.
  :param num1: Input number 1 | int or float
  :param num2: Input number 2 | int or float
  
  :return: num3: Sum of number | int or float
  '''

  num3 = num1 + num2
  return num3

# Syntax to get explanation/docstring from a particular module/function/class
print(sum_number.__doc__)




