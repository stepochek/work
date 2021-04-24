inputik = input(':')


def func(inputik):
    massiv = []
    a = 0
    for i in inputik:
        a += 1
        if a == 1:
            massiv.append(False)
        else:
            c = int(i) / int(inputik[a - 2])
            if c % 1 == 0:
                massiv.append(True)
            else:
                massiv.append(False)
    return massiv


print(func(inputik))