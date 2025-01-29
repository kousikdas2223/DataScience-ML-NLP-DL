import multiprocessing 
import time
from concurrent.futures import ProcessPoolExecutor

def square_numbers():
    for i in range(1, 10):
        time.sleep(0.1)
        print(f'Square of {i} is: {i**2}')

def cube_numbers():
    for i in range(1, 10):
        time.sleep(0.1)
        print(f'Cube of {i} is: {i**3}')

def cube_numbers2(num):
    for i in range(1, num):
        time.sleep(2)
        print(f'Cube of {i} is: {i**3}')

if __name__ == '__main__':

    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)

    print('Starting processes...')
    t = time.time()
    p1.start()
    p2.start()

    p1.join()
    p2.join()
    finished_time = time.time()

    print(f'Time taken: {finished_time - t} seconds')
    print('Both processes have finished.')

# Multi process executor execution

    print('Starting Multi processes...')
    t = time.time()
    with ProcessPoolExecutor() as executor:
        executor.map(cube_numbers2, range(1, 10))
        print('All processes have finished.')
    finished_time = time.time()
    print(f'Time taken: {finished_time - t} seconds')
    print('Both processes have finished.')




