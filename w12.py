primer = input('primer:')
spisok = [['ноль', 0], ['один', 1], ['два', 2], ['три', 3], ['четыре', 4], ['пять', 5], ['шесть', 6], ['семь', 7], ['восемь', 8], ['девять', 9]]
spisichok = []
spisichok.append(primer)
spisochok = spisichok[0].split(' ')
first = 0
znak = 0
second = 0
if spisochok[1] == 'плюс':
    znak = 1
else:
    znak = 0
print(znak)
for i in spisok:
    if i[0] in spisochok[0]:
        first = int(i[1])
print(first)
for j in spisok:
    if j[0] in spisochok[2]:
        second = int(j[1])
print(second)
if znak == 1:
    answ = first + second
else:
    answ = first - second
print(answ)