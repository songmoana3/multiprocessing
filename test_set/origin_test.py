import time
from tqdm import tqdm
from common_func import cpu_bound_tutorial


def main(count):

    # checking time
    init = time.time()

    # run process 
    results_pid = [cpu_bound_tutorial() for _ in tqdm(range(count))]
    elapsed_time = time.time() - init

    # show results
    print("********Origin Test********")    
    print('PID Count : ', len(set(results_pid)))
    print(f"Elapsed time : {elapsed_time}")