from multiprocessing.shared_memory import SharedMemory
from time import sleep
import numpy as np

array = np.array([1,2,3],dtype=int)
shmm = SharedMemory(create = True,size= array.nbytes)
shmm_data = np.ndarray(
  array.shape,array.dtype,shmm.buf
)
shmm_data[:] = array
print(array.shape,array.dtype,shmm.name)
while True:
  shmm_data[:] = np.random.randint(0,10,size=shmm_data.shape)
  sleep(0.1)
