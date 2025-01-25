int_lst = [1,2,3,4]
iterator = iter(int_lst)
i=0

while True:
    try:
        element = next(iterator)
        print(f'Element at index {i}: {element}')
        i += 1
    except StopIteration:
        break

str_lst = ['Sachin', 'Sourav', 'Rahul', 'Zahir']
iterator = iter(str_lst)
i=0

while True:
    try:
        element = next(iterator)
        element = element.upper()
        print(f'Element at index {i}: {element}')
        i += 1
    except StopIteration:
        break