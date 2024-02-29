import os
  
def cpu_bound_tutorial():
    result = 0
    for i in range(4000000):
        result += i
    return os.getpid()
