import threading
import time
import random

# Create a lock
lock = threading.Lock()

# Shared function that can only be executed by one thread at a time
def critical_function(thread_name):
    with lock:  # Acquire the lock
        print(f"{thread_name} is entering the critical section.")
        # Simulate some work in the critical section
        time.sleep(random.uniform(0.5, 1.5))
        print(f"{thread_name} is leaving the critical section.")
    print('finished')

# Function that each thread will run
def thread_function(name):
    print(f'hello, start function {name}')
    time.sleep(2)
    print(f"{name} is trying to enter the critical section.")
    critical_function(name)

if __name__ == '__main__':
    # Create threads
    threads = []
    for i in range(5):  # Create 5 threads
        thread_name = f"Thread-{i + 1}"
        thread = threading.Thread(target=thread_function, args=(thread_name,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    print("All threads have finished.")