with open('text-5task.txt', 'w+') as txt:
    for n in range(1, 15):
        txt.write(str(n) + ' ')

with open('text-5task.txt', 'r') as txt:
    lis = map(int, (txt.read().split()))
    print(sum(lis))
