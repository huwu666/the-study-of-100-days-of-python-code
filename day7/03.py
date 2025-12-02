#寻找水仙花数

for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100 

    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)


#将一个不知道有多少位的正整数反转

num = int(input('num = '))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10 
print(reversed_num)