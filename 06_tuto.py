from time import sleep
import multiprocessing
import numpy as np
from shmm import gen_shmm_dict,get_shmm_data
N=10 


def _n_rejector(shmm,rejected_n,lock):
  matrix = get_shmm_data(**shmm)
  if rejected_n==2: print("A",matrix)
  while np.any(matrix==rejected_n):
    lock.acquire()
    matrix[matrix==rejected_n] = np.random.randint(0,N , matrix[matrix==rejected_n].shape)
    print(matrix)
    lock.release()

if __name__=='__main__':
  lock = multiprocessing.Lock()
  matrix = np.random.randint(0,N,size=(10,))
  shmm,shmm_data = gen_shmm_dict(matrix=matrix)
  mat1 = get_shmm_data(**shmm)
  
  print(shmm_data)
  processes = []
  processes.append(multiprocessing.Process(target=_n_rejector,kwargs={"shmm":shmm,"rejected_n":2,"lock":lock,}))
  processes.append(multiprocessing.Process(target=_n_rejector,kwargs={"shmm":shmm,"rejected_n":3,"lock":lock,}))
  processes.append(multiprocessing.Process(target=_n_rejector,kwargs={"shmm":shmm,"rejected_n":4,"lock":lock,}))
  processes.append(multiprocessing.Process(target=_n_rejector,kwargs={"shmm":shmm,"rejected_n":5,"lock":lock,}))
  processes.append(multiprocessing.Process(target=_n_rejector,kwargs={"shmm":shmm,"rejected_n":6,"lock":lock,}))

  for p in processes: p.start()
  for p in processes: p.join()
  print(shmm_data)
  
  shmm_data = get_shmm_data(**shmm)

  # # Cleanup: Close and unlink shared memory
  # shmm['shmm'].close()
  # shmm['shmm'].unlink()

