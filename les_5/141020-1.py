with open('fst_task.txt', 'w') as txt:
    while 1:
        text_add = input('Enter without data for exit,\nor enter data to write to the file: ')
        txt.writelines(text_add + '\n')
        if text_add == '':
            break
