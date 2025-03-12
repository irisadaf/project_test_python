import os
import time

# Function that runs normally
def worker():
    pid = os.getpid()        # Get the current process ID
    ppid = os.getppid()      # Get the parent process ID
    print(f"Function in Process with PID: {pid} and PPID: {ppid} is running.")
    time.sleep(60)           # Simulating work
    print(f"Function in Process with PID: {pid} has finished.")

if __name__ == '__main__':
    # Number of times to run the function
    num_runs = 5

    # Run the function normally
    for _ in range(num_runs):
        worker()

    print("All functions have finished.")