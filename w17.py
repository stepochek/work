inputik = input('')
with open('file.txt', 'r') as file:
    spisok = []
    for i in file:
        splitok = i.split('')


def chotka(i):
    spisok = []
    integer = 0
    if len(i) % 2 == 0:
        for j in i:
            if j == ' ':
                spisok.append(integer)
                integer = 0
            else:
                integer += 1
    return spisok


chotka(i)
print(spisok)

