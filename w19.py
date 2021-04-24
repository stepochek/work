spisok = ['1', 12, 3, '6', '1', '6', '9', 10, '41']


def func(spisok):
    a = 0
    b = 0
    spisokk = []
    spisoknorm = []
    stroka = ''
    for p in spisok:
        spisokk.append(str(p))
    for i in spisok:
        r = str(i)
        for g in r:
            for j in g:
                if len(g) == 1:
                    if str(g) != '1':
                        if isinstance(spisok[a], int):
                            spisoknorm.append(int(g))
                        else:
                            spisoknorm.append(g)
                    else:
                        if len(spisokk) >= len(spisoknorm) + 1 and len(spisokk[a]) == 1:
                            if isinstance(spisok[a], int):
                                spisoknorm.append(None)
                            else:
                                spisoknorm.append('None')
        a += 1
    return spisoknorm


print(func(spisok))