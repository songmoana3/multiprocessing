import time
import multiprocessing
from tqdm import tqdm
from common_func import show_result, img_func


def main(count):
    
    init = time.time()
    
    with multiprocessing.Pool(8) as pool:
        results = pool.starmap(img_func, [() for _ in tqdm(range(count))])
    
    elapsed_time = time.time() - init
    
    show_result("Multiprocessing", results, elapsed_time)
