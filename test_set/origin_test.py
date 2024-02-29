import time
from tqdm import tqdm
from common_func import cpu_bound_tutorial


def main(count):

    # checking time
    start = time.time()

    # run process 
    results_pid = [cpu_bound_tutorial() for _ in tqdm(range(count))]

    # show results
    print("********Origin Test********")    
    print('PID Count : ', len(set(results_pid)))
    print('Elapsed time : ', time.time() - start)