import multiprocessing
from multiprocessing import Process
from time import sleep
import datetime
import os 
import numpy as np 

# Define a function to be executed by the process
def worker_function():
  print("PID ",os.getpid())
  sleep(1)

if __name__=='__main__':
  Ntasks = 20
  Njobs= 10
  processes = []
  beg = datetime.datetime.now()
  iter = 0 
  while iter<Ntasks:
    if np.sum([1 for p in processes if p.is_alive()])<Njobs:
      processes.append(Process(target=worker_function))
      processes[-1].start()
      iter+=1
    else: 
      for ind,p in enumerate(processes): 
        if not p.is_alive():
          p.close()
          processes.pop(p)
    
  for p in processes: p.join()
  
  end = datetime.datetime.now()
  
  print(
    "Total time",np.abs((beg-end).total_seconds()),"seconds"
    )