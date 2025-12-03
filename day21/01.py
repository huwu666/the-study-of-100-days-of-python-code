'''
文件读写与异常处理

实际开发过程中常常会遇到对数据进行持久化的场景,所谓持久化
是指数据无法长久保存的存储介质,实现数据持久化最简单直接的
方式就是通过文件系统将数据保存到文件中

计算机的文件系统是一种存储与组织计算机数据的方法,它使得对数据
的访问与查找变得容易,文件系统使用文件和树形目录的抽象逻辑
概念代替了物理设备的数据块概念
'''

file = open('day21/致橡树.txt', 'r', encoding = 'utf - 8')
print(file.read())
file.close

file = open('day21/致橡树.txt', 'r', encoding = 'utf - 8')
for line in file:
    print(line, end='')
file.close()

file = open('day21/致橡树.txt', 'a', encoding = 'utf - 8')
file.write('\n标题: 致橡树 ')
file.write('\n作者: 舒婷 ')
file.write('\n时间:1977.3')
file.close()