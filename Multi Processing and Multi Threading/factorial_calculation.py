"""
Factorial calculations, especially large numbers are CPU bound.
Multi processing can be used to distribute work loads across multiple cores.
"""

import multiprocessing
import math
import sys
import time

sys.set_int_max_str_digits(100000)


def factorial(number):
    print(f"computing factorial of {number}")
    result = math.factorial(number)
    # print(f"factorial of {number} = {result}")
    return result


if __name__ == "__main__":
    numbers = [99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999]

    start_time = time.time()
    for number in numbers:
        factorial(number)
    end_time = time.time()
    # print(f"results = {results}")
    print(f"Time taken = {end_time - start_time}")

    start_time = time.time()
    with multiprocessing.Pool() as pool:
        results = pool.map(factorial, numbers)
    end_time = time.time()
    # print(f"results = {results}")
    print(f"Time taken = {end_time - start_time}")
