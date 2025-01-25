int_lst = [1,2,3,4]

def int_func():
    for i in int_lst:
        print(f'Element at index {i-1}: {i}')
        yield i*i # This statement will generate a Generator

str_lst = ['Sachin', 'Sourav', 'Rahul', 'Zahir']

def str_func():
    i = 0
    for str in str_lst:
        print(f'Element at index {i}: {str}')
        i += 1
        yield str.upper() # This statement will generate a Generator


int_gen = int_func()
str_gen = str_func()

print(type(int_gen))
print(type(str_gen))

# Printing the elements using the generated Generators
i=0
while True:
    try:
        element = next(int_gen)
        print(f'Square of the element at index {i}: {element}')
        i += 1
    except StopIteration:
        break

i=0
while True:
    try:
        element = next(str_gen)
        print(f'Upper case of the element at index {i}: {element}')
        i += 1
    except StopIteration:
        break