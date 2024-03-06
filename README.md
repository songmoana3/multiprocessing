# Multiprocessing R&D
> Researcher : songmoana  
> Date : 24.03.06  
> Contact : je.song@interxlab.com

## _Research for ..._
- efficient multi-processing library

## _Test Set_
1. Circulation test set (complex computation)
2. image test set (Using HTTP conversation, image I/O)

## _Structure_
```
.
├── README.md
├── circulation_test_set
│   ├── multi_processing_test.py
│   ├── origin_test.py
│   └── ray_test.py
├── common_func.py
├── decode.py
├── encode.py
├── image_test_set
│   ├── multi_main.py
│   ├── origin_main.py
│   └── ray_main.py
└── main.py
```

## _How to execute_
1. Edit main.py file
    - Uncomment test set that you want to test
    
2. `$python main.py`

    - If you want to test image test set, you need to execute encode, decode code first.  
        `$python encode.py` and `$python decode.py`.
