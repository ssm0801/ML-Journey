# When to use it ?

# - IO bound tasks
# - Concurrent executions

import threading
import time


def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number: {i}")


def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter: {letter}")


start_time = time.time()
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letter)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
end_time = time.time()
print(f"Time taken: {end_time - start_time}")
