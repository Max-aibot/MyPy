import re

with open('151020-6.txt', 'r+', encoding='utf-8') as txt:
    dic = {}
    for lines in txt:
        nums = re.findall(r'\d+', lines)
        nums = sum([int(i) for i in nums])
        for a in lines:
            a = lines.split()
            n = {a[0]: nums}
            dic.update(n)

    print(dic)
