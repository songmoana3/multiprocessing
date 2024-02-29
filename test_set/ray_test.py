import os
import ray
import time
from tqdm import tqdm


def main(count):

    # init setting
    ray.init(num_cpus=8) # core 8

    # checking time
    init = time.time()

    @ray.remote
    def cpu_bound_tutorial():
        result = 0
        for i in range(4000000):
            result += i
        return os.getpid()

    result_ids = [cpu_bound_tutorial.remote() for _ in tqdm(range(count))]

    # run process and return results
    result = ray.get(result_ids)
    
    # show results
    print("********Ray Test********")
    print('PID Count : ', len(set(result)))
    print('Elapsed time', time.time() - init)

    ray.shutdown()
