import time

def record_time(func):
    def wraaper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{end - start}')
        return result
    
    return wraaper

'''
在python中,装饰器就是解决这类问题的最佳选择
通过装饰器语法,我们可以把原来的业务没有关系
计时功能的代码封装到一个函数中
'''