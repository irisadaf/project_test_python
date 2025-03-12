import threading
import os
import time

# Function that runs in each thread
def worker():
    pid = os.getpid()        # Get the current process ID
    ppid = os.getppid()      # Get the parent process ID
    print(f"Thread in Process with PID: {pid} and PPID: {ppid} is running.")
    time.sleep(60)           # Simulating work
    print(f"Thread in Process with PID: {pid} has finished.")

if __name__ == '__main__':
    # Number of threads
    num_threads = 5
    pid = os.getpid()  # Get the current process ID
    ppid = os.getppid()  # Get the parent process ID
    print(f"main Process with PID: {pid} and PPID: {ppid} is running.")
    # List to hold the threads
    threads = []

    # Create and start the threads
    for _ in range(num_threads):
        thread = threading.Thread(target=worker)
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    print("All threads have finished.")

    time.sleep(20)  # Simulating work
    print(f"main Process with PID: {pid} has finished.")