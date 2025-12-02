'''
如果想逐个取出列表中的元素,可以使用for-in循环
有一下两种做法
'''

languages = ['python', 'java', 'c++', 'kotlin']
for index in range(len(languages)):
    print(languages[index])

for language in languages:
    print(language)