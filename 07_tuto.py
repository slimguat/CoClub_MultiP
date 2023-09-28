from multiprocessing.shared_memory import SharedMemory
from time import sleep
import numpy as np
import multiprocessing
import datetime as dt
import sys
if True:
  if len(sys.argv) != 3:
      print("Usage: python script.py <integer1> <integer2>")
      sys.exit(1)

  try:
      reject_i = int(sys.argv[1])
      reject_j = int(sys.argv[2])
  except ValueError:
      print("Both arguments must be integers.")
      sys.exit(1)

N=10 
def _n_rejector(shmm,rejected_n,lock):
  matrix = np.ndarray(shmm[0],shmm[1],shmm[2].buf)
  beg = dt.datetime.now()
  while np.abs((beg-dt.datetime.now()).total_seconds())<0.2:
    if matrix[matrix==rejected_n].shape[0]!=0:
      lock.acquire()
      matrix[matrix==rejected_n] = np.random.randint(0,N,size=matrix[matrix==rejected_n].size)
      lock.release()
      print(matrix)
      beg = dt.datetime.now()
    else:
      pass
  
if __name__ == "__main__":
  lock = multiprocessing.Lock()
  
  matrix = np.random.randint(0,N,size=(10,))
  shmm = SharedMemory(create = True,size=matrix.nbytes)
  smdict = [
    matrix.shape,
    matrix.dtype,
    shmm,
  ]
  shmm_data  = np.ndarray(smdict[0],smdict[1],smdict[2].buf);shmm_data[:] = matrix
  print(shmm_data)
  
  processes = []
  for i in range(reject_i,reject_j):
    processes.append(multiprocessing.Process(target=_n_rejector,kwargs={"shmm":smdict,"rejected_n":i,"lock":lock,}))
  
  for p in processes: p.start()
  for p in processes: p.join()


  print(shmm_data)

  # Cleanup: Close and unlink shared memory
  shmm.close()
  shmm.unlink()
  
  
# def gen_shmm_dict(matrix):
#   shm = shared_memory.SharedMemory(create=True, size=matrix.nbytes)
#   shm_matrix = np.ndarray(shape=matrix.shape,dtype=matrix.dtype, buffer=shm.buf)
#   # return 0 
#   shm_matrix[:] = matrix
#   shmm_dict = {
#     'shape':shm_matrix.shape,
#     'dtype':shm_matrix.dtype,
#     'shmm' :shm
#     }
#   return shmm_dict,shm_matrix
# def get_shmm_data(shmm,shape,dtype):
#   shm_matrix = shared_memory.SharedMemory(create=False, name=shmm.name)
#   shm_matrix= np.ndarray(shape=shape,dtype=dtype, buffer=shm_matrix.buf)
#   return shm_matrix
