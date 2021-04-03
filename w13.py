spisok = [1, 4, 6, 3, 2, 4, 6, 1, 5, 7, 8]
ho = []
num = 0
for i in spisok:
    if i not in ho[0:-1]:
        num += 1
        ho.append(i)
spisok = []
for j in ho:
    spisok.append(j)
print(spisok, ho)