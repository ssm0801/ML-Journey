# When to use it ?

# - CPU bound tasks
# - Parallel process : use multiple cores


import multiprocessing
import time


def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square of {i}: {i*i}")


def cube_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Cube of {i}: {i*i*i}")


if __name__ == "__main__":
    start_time = time.time()
    process1 = multiprocessing.Process(target=square_numbers)
    process2 = multiprocessing.Process(target=cube_numbers)
    process1.start()
    process2.start()
    process1.join()
    process2.join()
    end_time = time.time()
    print(f"Time taken: {end_time - start_time}")
