#求100内的素数

for num in range(2, 100):
    is_prise = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prise = False
            break
    if is_prise:
        print(num)

        