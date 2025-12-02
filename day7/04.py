#百钱百鸡问题

for x in range(1, 21):
    for y in range(1, 34):
        for z in range(1, 301):
            if x + y + z == 100 and x * 5 + y * 3 + z // 3 == 100:
                print(x, y, z)