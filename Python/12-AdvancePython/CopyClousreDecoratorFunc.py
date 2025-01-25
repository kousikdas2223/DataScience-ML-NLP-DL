print("============Copy Example===========")

def parent_func():
    print('Parent Function')

def child_func():
        print('Child Function')

parent_func()
child_func()

# Copying the child function to parent function
parent_func=child_func

parent_func()
child_func()

# Changing the value of the child function
def child_func():
    print('Changed Child Function')

parent_func()
child_func()

# Deleting the child function
del child_func

parent_func()

# Trying to call the deleted child function

try:
    child_func()
except NameError as e:
    print(str(e))

# Closure Example
print("============Closure Example===========")

def outer_func(x):
    def inner_func(y):
        return x + y
    return inner_func

closure_func = outer_func(5)

print(closure_func(10))

def findStudent(studid):
     marks = {'Physics': 90, 'Chemistry': 80, 'Mathematics': 70}
     def getDetails(name, age):
         return f'Student ID: {studid}, Name: {name}, Age: {age}, Marks: {marks}'
     return getDetails

student1 = findStudent(101)

print(student1('Kousik Das', 20))

# Decorator Example
print("============Decorator Example===========")
def decorator_func(func):
    def wrapper_func(*args, **kwargs):
        print('Before calling the function')
        result = func(*args, **kwargs)
        print('After calling the function')

        return result
    return wrapper_func

@decorator_func
def display_info(name, age, marks):
    print(f'Name: {name}, Age: {age}, Marks: {marks}')

print(display_info('Kousik Das', 25, {'Physics': 90, 'Chemistry': 80, 'Mathematics': 70}))