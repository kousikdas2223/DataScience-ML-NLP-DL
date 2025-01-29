import threading
import time
import requests
from bs4 import BeautifulSoup


def print_numbers():
    for i in range(1, 11):
        print(f"The number is {i}")
        time.sleep(1)

def print_letters():
    for i in 'abcdefghij':
        print(f"The letter is {i}")
        time.sleep(0.5)

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t = time.time()
t1.start()
t2.start()

t1.join()
t2.join()

finished_time = time.time()

print(f"Total time taken: {finished_time - t} seconds")

# Multi thread executor execution

from concurrent.futures import ThreadPoolExecutor

def square_numbers(numbers):
    for i in range(1, numbers):
        time.sleep(0.1)
        print(f'Square of {i} is: {i*i}')
        
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
if __name__ == '__main__':
    t = time.time()
    with ThreadPoolExecutor(max_workers=3) as executor:
            results = executor.map(square_numbers, num)
    # for result in results:
    #     print(result)
    print(f'Time taken: {time.time() - t} seconds')


urls = [
     'https://python.langchain.com/v0.2/docs/introduction',
    'https://python.langchain.com/v0.2/docs/concepts',
    'https://python.langchain.com/v0.2/docs/tutorials'
]

def fetch_page(url):
     response = requests.get(url)
     soup = BeautifulSoup(response.text, 'html.parser')
     print(f'Fetched {(len(soup.text))} characters from {url}')

threads = []

for url in urls:
     t = threading.Thread(target=fetch_page, args=(url,))
     threads.append(t)
     t.start()

for thread in threads:
     thread.join()

print('All pages fetched')








