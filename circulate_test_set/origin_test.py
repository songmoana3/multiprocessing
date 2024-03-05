import time
from tqdm import tqdm
from common_func import cpu_bound_tutorial, show_result


def main(count):

    # checking time
    init = time.time()

    # run process 
    results_pid = [cpu_bound_tutorial() for _ in tqdm(range(count))]
    elapsed_time = time.time() - init

    # show results
    show_result("Origin", results_pid, elapsed_time)