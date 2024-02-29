
import time
import multiprocessing
from tqdm import tqdm
from common_func import cpu_bound_tutorial


def main(count):
    
    # # checking time
    init = time.time()
    
    # run process
    with multiprocessing.Pool(8) as pool:
        results = pool.starmap(cpu_bound_tutorial, [() for _ in tqdm(range(count))])
        
    elapsed_time = time.time() - init
    
    # # show results
    print("********Multiprocessing Test********")    
    print('PID Count : ', len(set(results)))
    print(f"Elapsed time : {elapsed_time}")
