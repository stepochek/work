stroka = input(':')


def func(stroka):
    a = 0
    vrem = []
    for i in stroka:
        a += 1
        if stroka[a].isdigit() or stroka[a - 2].isdigit():
            vrem.append(i)
        else:
            if not i.isdigit():
                a += int(vrem[0])
                vrem = []
            else:
                a += int(i)
    return a


print(func(stroka))