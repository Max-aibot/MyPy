import json


with open('151020-7.txt', 'r+', encoding='utf-8') as txt:

    margin = {}
    for lines in txt:
        for a in lines:
            a = lines.split()
            n = {a[1] + '_' + a[0]: int(a[2]) - int(a[3])}
            margin.update(n)

    count = 0
    summer = 0
    for n in margin.values():
        count += 1
        summer += int(n)

    av_marg = {'Average margin': summer / count}
    lis = [margin, av_marg]

    with open('151020-7.json', 'w') as jf:
        json.dump(lis, jf)

with open('151020-7.json') as jf:
    data = json.load(jf)
    print(data)
