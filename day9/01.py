languages = ['python', 'java', 'c++']
languages.append('javascript')
print(languages)
languages.insert(1, 'sql')
print(languages)

if 'java' in languages:
    languages.remove('java')
if 'swift' in languages:
    languages.remove('swift')
print(languages)
languages.pop()
temp = languages.pop(1)
print(temp)
languages.append(temp)
print(languages)
languages.clear()
print(languages)

items = ['python', 'java', 'c++']
del items[1]
print(items)

items = ['python', 'java', 'java', 'c++', 'kotlin', 'python']
print(items.index('python'))
print(items.index('python', 1))
print(items.count('python'))
print(items.count('kotlin'))
print(items.count('swfit'))

