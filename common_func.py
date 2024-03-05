import os
import requests  
  
def cpu_bound_tutorial():
    result = 0
    for i in range(4000000):
        result += i
    return os.getpid()


def show_result(name, result, time):
    
    print(f"********{name} Test********")
    print(f"PID Count : {len(set(result))}") # drop duplicated
    print(f"Elapsed time : {time}")
    

def img_func():
    
    url = "http://localhost:8000/encode"
    
    base_root = "/home/songmoana/Downloads/choonsik.jpg"

    with open(base_root, 'rb') as f:
        files = {"upload_image": f}
        res = requests.post(url, files=files)   
        if res.status_code == 200:
            pass
        else:
            raise Exception
        
    return os.getpid()
