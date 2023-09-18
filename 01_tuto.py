import multiprocessing
import os 
import sys
import datetime
from time import sleep 
import numpy as np

if len(sys.argv)<=1:
  Njobs = 1
else:Njobs = int(sys.argv[1])

def calculate_square(number):
    result = number * number
    # print(f"The square of {number} is {result}. PID: {os.getpid()}")
    sleep(1)
    
    
if __name__ == "__main__":
  N = 20
  numbers = np.arange(N)
  time = datetime.datetime.now()
  with multiprocessing.Pool(processes=Njobs) as pool:
    pool.map(calculate_square, numbers)
  print(f"Total execution time: {np.abs((time-datetime.datetime.now()).total_seconds()):5.2f}")
  