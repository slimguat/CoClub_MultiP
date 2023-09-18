import multiprocessing

# Define a function to be executed by the process
def worker_function(name):
    print(f"Hello, {name}!")

if __name__=='__main__':
  # Create a multiprocessing.Process instance
  process1 = multiprocessing.Process(target=worker_function, args=("Charlie the Harley",))
  process2 = multiprocessing.Process(target=worker_function, kwargs={"name":"Sophie the trophy"})
  process3 = multiprocessing.Process(target=worker_function, args=("Albert the shepherd",))
  
  # Start the process
  process1.start()
  process2.start()
  process3.start()

  # Wait for the process to finish (optional)
  process1.join()
  process2.join()
  process3.join()

  print("Main program continues...")