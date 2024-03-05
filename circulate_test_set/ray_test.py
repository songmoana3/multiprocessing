import ray
import time
from tqdm import tqdm
from common_func import cpu_bound_tutorial, show_result


def main(count):

    # init setting
    ray.init(num_cpus=8) # core 8

    # checking time
    init = time.time()

    # @ray.remote
    # def cpu_bound_tutorial():
    #     result = 0
    #     for i in range(4000000):
    #         result += i
    #     return os.getpid()
    
    # result_ids = [cpu_bound_tutorial.remote() for _ in tqdm(range(count))]

    remote_cpu_bound_tutorial = ray.remote(cpu_bound_tutorial)

    result_ids = [remote_cpu_bound_tutorial.remote() for _ in tqdm(range(count))]

    # run process and return results
    result = ray.get(result_ids)
    elapsed_time = time.time() - init
    
    # show results
    show_result("Ray", result, elapsed_time)

    ray.shutdown()


if __name__ == "__main__":
    main(count=500)