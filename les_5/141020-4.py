with open('text.txt', 'r') as txt:
    file = txt.read().replace('One', 'Один').replace('Two', 'Два').replace('Three', 'Три').replace('Four', 'Четыре')
    file = file.replace('One', 'Один')

    with open('texttow.txt', 'w+') as txtw:
        txtw.write(file)
