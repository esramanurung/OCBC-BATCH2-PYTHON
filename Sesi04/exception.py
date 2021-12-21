'''
import sys
assert ('linux' in sys.platform), "This code runs on Linux only."
assert ('windows' in sys.platform), "This code runs on Windows only."
'''
import sys
print(sys.platform)
def os_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    assert ('windows' in sys.platform), "This code runs on Windows only."
    print('Doing something.')

# os_interaction()
try:
    os_interaction()
except:
    print('Windows function was not executed\n')

##The AssertionError Exception: Handling Exception
import sys
print(sys.platform)
def os_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    assert ('windows' in sys.platform), "This code runs on Windows only."
    print('Doing something.')
try:
    os_interaction()
except AssertionError as error:
    print("##",error)
    print('The os_interaction() function was not executed\n')

## 
try:
    with open('file.log') as file:
        read_data = file.read()
except:
    print('Could not open file.log')
    print('file.log is not find in this directory\n')


# Exception FileNotFoundError
try:
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)

##With Else Clause
import sys
print(sys.platform)
def os_interaction():
    #assert ('linux' in sys.platform), "Function can only run on Linux systems."
    assert ('win32' in sys.platform), "This code runs on Windows only."
    print('Doing something.')

try:
    os_interaction()
except AssertionError as error:
    print(error)
else:
    print('Executing the else clause.\n')

##You can also try to run code inside the else clause and catch possible exceptions there as well:
import sys
print(sys.platform)
def os_interaction():
    #assert ('linux' in sys.platform), "Function can only run on Linux systems."
    assert ('win32' in sys.platform), "This code runs on Windows only."
    print('Doing something.')

try:
    os_interaction()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)

## Cleaning Up After Using finally
import sys
print(sys.platform)
def os_interaction():
    #assert ('linux' in sys.platform), "Function can only run on Linux systems."
    assert ('win32' in sys.platform), "This code runs on Windows only."
    print('Doing something.')

try:
    os_interaction()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('Cleaning up, irrespective of any exceptions.')
    print('end')
