import time
# os
import os

print(os.getcwd())
print(os.name)


# filter(함수, 리스트) : 함수로 반환되는 값만 걸러줌
def positive(x):
    return x > 0


print(list(filter(positive, [1, -3, 2, 0, 4, -6])))

# enumerate : (인덱스, 값) 반환
my_list = ['body', 'foo', 'bar']
for i, name in enumerate(my_list):
    print(i, name)


def get_time():
    start = time.time()
    for i in range(30):
        print(i, end=' ')
    print()
    end = time.time()
    print('걸린시간:', end-start, "초")


get_time()
