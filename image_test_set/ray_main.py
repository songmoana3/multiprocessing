import ray
import time
from tqdm import tqdm
from common_func import show_result, img_func

def main(count):
    
    init = time.time()
    
    img_func_remote = ray.remote(img_func)
    
    result_ids = [img_func_remote.remote() for _ in tqdm(range(count))]
    result = ray.get(result_ids)
    elapsed_time = time.time() - init
    
    show_result("Ray", result, elapsed_time)
    ray.shutdown()