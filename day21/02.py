'''为了让代码具有健壮性与容错性,我们可以使用python的异常
机制对可能在运行时发生状况的代码进行适当的处理'''

file = None
try:
    file = open('致橡树.txt', 'r', encoding = 'utf - 8')
except FileNotFoundError:
    print('无法打开指定文件')
except LookupError:
    print('指定了未知的编码')
except UnicodeDecodeError:
    print('读取文件时解码错误')
finally:
    if file:
        file.close()