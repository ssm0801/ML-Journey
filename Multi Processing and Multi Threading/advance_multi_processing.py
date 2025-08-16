# Multithreading with Thread Pool Executor

from concurrent.futures import ProcessPoolExecutor
import time


def sqaure_number(number):
    time.sleep(2)
    return f"Sqaure of {number}: {number * number}"


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if __name__ == "__main__":
    start_time = time.time()
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(sqaure_number, numbers)
    end_time = time.time()

    for result in results:
        print(result)

    print(f"Time taken: {end_time - start_time}")
