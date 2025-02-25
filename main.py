from typing import Union
from fastapi import FastAPI

import time
import numpy as np
import random


app = FastAPI()


@app.get("/")
def read_root():
    a = [1,2,3,4]
    b = [5,6,7,8]
    # TODO a + b
    # result = [x + y for x, y in zip(a, b)]
    # return {"Hello": result}
    result = [] 
    for i in range(len(a)):
        result.append(a[i] + b[i])
    return {"Hello": result}

@app.get("/two-dimensional-array")
def two_dimensional_array():
    a = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    b = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]

    # result = []
    # # TODO

    # return {"result": result}

# $ curl http://localhost:8000/two-dimensional-array
# {
# "result": [
#     [10, 10, 10],
#     [10, 10, 10],
#     [10, 10, 10]
# ]
#}

    result = []
    for i in range(len(a)):  # 행 순회
        row = []
        for j in range(len(a[0])):  # 열 순회
            row.append(a[i][j] + b[i][j])  # 같은 위치의 요소 더하기
        result.append(row)
    return {"result": result}       


@app.get("/add-large-arrays")
def add_large_arrays():
    
    N = 10**6  # 100만 개 요소

    # 랜덤한 1차원 배열 2개 생성
    start_time = time.time()
    a = [random.randint(0, 100) for _ in range(N)]   
    b = [random.randint(0, 100) for _ in range(N)]
    end_time = time.time()
    
    # 실행 시간 측정 시작
    add_start_time = time.time()
    
    # 요소별 덧셈
    result = []
    for x, y in zip(a, b):
        result.append(a + b)

    # 실행 시간 측정 종료
    add_end_time = time.time()
    
    
    # 수행  시간 리턴
    return {"execution_time": end_time - start_time}


@app.get("/add-large-arrays-choice")
def add_large_arrays_choices():
    
    N = 10**6  # 100만 개 요소

    # 랜덤한 1차원 배열 2개 생성
    start_creation_time = time.time()
    a = random.choice(range(101), k=N)  ## 랜덤초이스로 바꿔서 속도 비교 
    b = random.choice(range(101), k=N)
    end_creation_time = time.time()
    
    # 실행 시간 측정 시작
    add_start_time = time.time()
    
    # 요소별 덧셈
    result = []
    for x, y in zip(arr1, arr2):
        result.append(a + b)

    # 실행 시간 측정 종료
    add_end_time = time.time()
    
    # 수행 시간 리턴
    # 리턴값: 배열 생성 시간(array_creation_time)과 덧셈 수행(addition_time) 시간을 각각 리턴
    return {
        "execution_time": end_creation_time - start_creation_time,
        "execution_time": add_end_time - add_start_time
        }
    
    ## TODO add_large_array() 를 고차 함수를 이용해서 중복코드 제거
    ## STEP 1
    ### def add_arrays(N, generate_random_array): -> 라는 함수를 만든다
    ### 위 함수의 리턴값은 array_creation_time, addtion_time 이다
    ### def generate_random_array_wirh_randint(N): -> 함수와 아래 함수를 만든다
    ### def generate_random_array_wirh_choices(N):
    ### 위 두 함수의 리턴값은 list이다
    ### 그리고 조합한다.
    
    def add_arrays(N, generate_random_array):
        return 
    
    
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
        
    
    
    
  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    