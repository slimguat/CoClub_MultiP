import multiprocessing
from time import sleep
import numpy as np
import datetime

def multiply_and_print_pid(a, b):
    import os  # Import os module to access the PID
    result = a * b
    sleep(1)
    pid = os.getpid()
    print(f"PID {pid}: {a} * {b} = {result}")
    return result

if __name__ == "__main__":
    # Create a multiprocessing Pool with 4 processes
    pool = multiprocessing.Pool(processes=4)

    # Define a list of argument tuples for the function
    arguments = [(2, 3), (4, 5), (6, 7)]

    # Use apply_async to submit tasks and get the results asynchronously
    time = datetime.datetime.now()
    results = [pool.apply_async(multiply_and_print_pid, args=(a, b)) for a, b in arguments]
    print(f"Process starting time: {np.abs((time-datetime.datetime.now()).total_seconds()):5.2f}")
    
    
    # Close the pool and wait for all tasks to complete
    pool.close()
    pool.join()
    print(f"Total execution time: {np.abs((time-datetime.datetime.now()).total_seconds()):5.2f}")

    # Retrieve and print the results
    final_results = [result.get() for result in results]
    print("Final results:", final_results)
