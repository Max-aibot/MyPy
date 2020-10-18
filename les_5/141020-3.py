with open('141020-3.txt', 'r+') as txt:
    money = {}
    line_count = 0

    for lines in txt:
        line_count += 1
        for a in lines:
            a = lines.split()
            n = {a[0]: int(a[1])}
            money.update(n)

    summer = 0
    for k, v in money.items():
        summer += int(v)
        if v < 20000:
            print(k)
    print(f'''Получают меньше 20 000 тугриков,\na cредняя зарплата сотрудников:
{(summer / line_count):.02f} тугриков...\nМожно и получше...''')
