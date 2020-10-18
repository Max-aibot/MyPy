with open('141020-2.txt') as txt:
    lines = 0
    words = 0
    for li in txt:
        lines += 1
        for w in li.split():
            words += 1

    print(lines, words)
