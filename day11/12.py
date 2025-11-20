#查找操作

s = 'hello, world!'

print(s.find('or'))
print(s.find('or', 9))
print(s.find('of'))
print(s.index('or'))
#print(s.index('or', 9))

#以下为从后向前查找

print(s.find('o'))
print(s.rfind('o'))
print(s.rindex('o'))