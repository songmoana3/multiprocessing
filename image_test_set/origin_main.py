import time
from tqdm import tqdm
from common_func import show_result, img_func


def main(count):
    
    init = time.time()
    result_ids = [img_func() for _ in tqdm(range(count))]
    elapsed_time = time.time() - init
    
    show_result("Origin", result_ids, elapsed_time)
