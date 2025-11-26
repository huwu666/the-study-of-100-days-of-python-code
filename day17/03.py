#语法糖

import random
import time

def record_time(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{end - start}')

        return result
    return wrapper

@record_time
def download(filename):
    print(f'开始下载{filename}.')
    time.sleep(random.random() * 6)
    print(f'{filename}下载完成 ')

@record_time
def upload(filename):
    print(f'开始上传{filename}')
    time.sleep(random.random() * 8)
    print(f'{filename}上传完成 ')

download('mysql从删库到跑路.avi')
upload('python从入门到住院')