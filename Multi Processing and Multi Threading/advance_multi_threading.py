# Multithreading with Thread Pool Executor

from concurrent.futures import ThreadPoolExecutor
import time


def print_numbers(i):
    time.sleep(2)
    return f"Number: {i}"


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

start_time = time.time()
with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_numbers, numbers)
end_time = time.time()

for result in results:
    print(result)

print(f"Time taken: {end_time - start_time}")
