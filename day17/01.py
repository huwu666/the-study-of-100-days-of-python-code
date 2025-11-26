#用一个函数装饰另外一个函数并为其提供额外的能力

import random
import time

def download(filename):
    print(f'开始记载{filename}')
    time.sleep(random.random() * 6)
    print(f'{filename}下载完成 ')

def upload(filename):
    print(f'开始上传{filename}')
    time.sleep(random.random() * 8)
    print(f'{filename}上传完成 ')

start = time.time()
download('mysql从删库到跑路 ')
end = time.time()
print(f'花费时间:{end - start:.2f}秒')
start = time.time()
upload('python从入门到住院')
end = time.time()
print(f'花费时间:{end - start:.2f}')