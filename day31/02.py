names = ['guanyu', 'zhangfei', 'zhaoyun', 'machao', 'huangzhong']
courses = ['yuwen', 'shuxue', 'yingyu']

scores = [[None] * len(courses) for _ in range(len(names))]
for row, name in enumerate(names):
    for col, course in enumerate(courses):
        scores[row][col] = float(input(f'qingshuru{name}de{course}chengji'))
        print(scores)

        