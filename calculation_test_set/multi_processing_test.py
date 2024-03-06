
import time
import multiprocessing
from tqdm import tqdm
from common_func import cpu_bound_tutorial, show_result


def main(count):
    
    # # checking time
    init = time.time()
    
    # run process
    with multiprocessing.Pool(8) as pool:
        results = pool.starmap(cpu_bound_tutorial, [() for _ in tqdm(range(count))])
        
    elapsed_time = time.time() - init
    
    # # show results
    show_result("Multi-Processing", results, elapsed_time)
