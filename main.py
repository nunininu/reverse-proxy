from typing import Union

from fastapi import FastAPI

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

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
