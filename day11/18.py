#字符串的拆分与合并

s = 'i love you'
words = s.split()

print(words)
print('~'.join(words))


s = 'I#love#you#so#much'
words = s.split('#')
print(words)  # ['I', 'love', 'you', 'so', 'much']
words = s.split('#', 2)
print(words)  # ['I', 'love', 'you#so#much']