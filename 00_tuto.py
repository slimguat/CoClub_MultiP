import multiprocessing
import os 
import sys
import datetime
from time import sleep 
import numpy as np

if len(sys.argv)<=1:
  
  mlp = True
else:mlp = bool(float(sys.argv[1]))
Njobs = 14

def calculate_square(number):
    result = number * number
    print(f"The square of {number} is {result}. PID: {os.getpid()}")
    sleep(1)
if __name__ == "__main__":
  print(sys.argv,mlp)
  print(f"{'With' if mlp else 'No'} multiprocessing" )
  numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  if mlp:
    time = datetime.datetime.now()
    with multiprocessing.Pool(processes=Njobs) as pool:
        pool.map(calculate_square, numbers)
    print("Total execution time: ",np.abs((time-datetime.datetime.now()).total_seconds()))
    
  else:
    time = datetime.datetime.now()
    [calculate_square(number) for number in numbers]
    print("Total execution time: ",np.abs((time-datetime.datetime.now()).total_seconds()))
    