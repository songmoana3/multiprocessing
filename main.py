import os
from dotenv import load_dotenv
from circulate_test_set import origin_test, multi_processing_test, ray_test
from image_test_set import origin_main, ray_main, multi_main


load_dotenv()

class MProcessingTest:
    
    def __init__(self):
        self.count = int(os.getenv("COUNT"))
        
    def run_process(self, func):
        func(self.count)
        
        

if __name__== "__main__":
    
    test = MProcessingTest()
    # test.run_process(origin_test.main)
    # test.run_process(multi_processing_test.main)
    # test.run_process(ray_test.main)
    
    
    test.run_process(origin_main.main)
    test.run_process(ray_main.main)
    test.run_process(multi_main.main)