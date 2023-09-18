import multiprocessing
import os 
import sys
import datetime
from time import sleep 
import numpy as np

if len(sys.argv)<=1:
  Njobs = 1
else:Njobs = int(sys.argv[1])

def calculate_square(a,b):
    result = a * b
    print(f"{a:02d}x{b:02d}={result:02d}| PID: {os.getpid()}")
    sleep(1)
    
    
if __name__ == "__main__":
  N = 3
  numbers = (np.random.random([N,2])*10).astype(int)
  print("Argument list number of Jobs X length of argument list",numbers,sep='\n')
  time = datetime.datetime.now()
  with multiprocessing.Pool(processes=Njobs) as pool:
    pool.starmap(calculate_square, numbers)
  print(f"Total execution time: {np.abs((time-datetime.datetime.now()).total_seconds()):5.2f}")
  