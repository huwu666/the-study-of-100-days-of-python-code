'''
分支结构与循环结构是构造程序逻辑的基础
看懂别人的代码很容易,但是要写出类似的代码却很难
这是因为相应的练习量还没有达到让你可以随心所欲写出代码的程度
'''

#例子一:求100以内的素数

for num in range(2, 100):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)