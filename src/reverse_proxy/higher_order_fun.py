import time

def square(x):
    return x**2

def double(x):
    return x*2

nums = [1, 2, 3, 4, 5]

# def num_square(nums):
#     # 리스트 각각의 갑에 제곱을 하여 프린트
#     start_time = time.time()
#     print([square(x) for x in nums])
#     end_time = time.time()
#     print(end_time - start_time)
#     # for x in nums: nums = p[1, 2, 3, 4, 5]
#     # print([nums])

# def num_double(nums):
#     # 리스트 각각의 갑에 2배 곱하여 프린트
#     start_time = time.time()
#     print([double(x) for x in nums])
#     end_time = time.time()
#     print(end_time - start_time)
#     # print([nums])
    
def num_cal(data, fun): # 이 함수를 쓰면 위에 있는 square, double 안 써도 됨
    # TODO 고차 함수로
    start_time = time.time()
    print([fun(x) for x in nums])
    end_time = time.time()
    print(end_time - start_time)
    # print([nums])

num_cal(nums, square)
num_cal(nums, square)