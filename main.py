from typing import Union
from fastapi import FastAPI

import time
import numpy as np
import random


app = FastAPI()


# 상수
# N = 10**5  # 10만 개 요소
N = 10**4  # 1만 개 요소

@app.get("/add-count-large-arrays-python")
# 문제 3
def add_large_arrays_python():
    start_creation_time = time.time()
    a, b = gen_r_array_choices(N)
    end_creation_time = time.time()

    add_start_time = time.time()
    plus_py(a,b)
    add_end_time = time.time()

    array_creation_time = end_creation_time - start_creation_time
    addition_time = add_end_time - add_start_time
    return array_creation_time, addition_time

@app.get("/add-count-large-arrays-numpy")
def add_large_arrays_numpy():
    start_creation_time = time.time()
    a, b = gen_r_array_numpy(N)
    end_creation_time = time.time()

    add_start_time = time.time()
    plus_numpy(a,b)
    add_end_time = time.time()

    array_creation_time = end_creation_time - start_creation_time
    addition_time = add_end_time - add_start_time
    return array_creation_time, addition_time

def gen_r_array_choices(N):
    a = random.choices(range(101), k=N)
    b = random.choices(range(101), k=N)
    return a, b

def gen_r_array_numpy(N):
    a = np.random.randint(1, 101, size=N)  # 1 이상 100 이하의 정수
    b = np.random.randint(1, 101, size=N)
    return a,b

def plus_py(a, b):
    result = []
    for x, y in zip(a, b):
        result.append(x + y)
    return result

def plus_numpy(a, b):
    return a + b


# N = 10**2

# # @app.get("/api/py/gen_r_array_choices")
# def get_gen_r_array_choices(N):
#     a = random.choices(range(101), k=N)
#     b = random.choices(range(101), k=N)
#     return a, b

# @app.get("/api/py/plus_py")
# def get_plus_py():
#     a, b = get_gen_r_array_choices(N)
#     result = plus_py(a, b)
#     return result

# @app.get("/api/py/plus_numpy")
# def gen_r_array_numpy():
#     a = np.random.randint(1, 101, size=N)  # 1 이상 100 이하의 정수
#     b = np.random.randint(1, 101, size=N)
#     a, b = gen_r_array_numpy(N)
#     return plus_numpy(a, b)


# @app.get("/우웩")
# def gen_r_array_choices(N):
#     a = random.choices(range(101), k=N)
#     b = random.choices(range(101), k=N)
#     return a, b

# def gen_r_array_numpy(N):
#     a = np.random.randint(1, 101, size=N)  # 1 이상 100 이하의 정수
#     b = np.random.randint(1, 101, size=N)
#     return a,b

# def plus_py(a, b):
#     result = []
#     for x, y in zip(a, b):
#         result.append(x + y)
#     return result

# def plus_numpy(a, b):
#     return (a + b).tolist()
    
    
    
  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
