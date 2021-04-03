stroka = 'ya 123 4443 iz afr6iki ya priyexal chobi pit zakamskiy kvas'
spisokchisel = {}
chislo = 0
spisok = stroka.split()
for i in spisok:
    a = 0
    for j in i:
        if i == j:
            chislo += 1
            spisokchisel[i] = chislo

#def printt(stroka):
#    b = ''
#    a = 0
#    c = 1
#    for i in stroka:
#        if i.isdigit() and id(i) != id(stroka[0]) and i[a - c] == ' ':
#            a += 1
#            if i != ' ':
#                c += 1
#            print("int")
#        else:
#            a += 1
#            b += i
#    return b
#print(printt(stroka))


cifri = 1234
def ahaha(chisloo):
    tsifra= 0
    b = ''
    stepa = 0
    a = 0
    for i in str(chisloo):
        tsifra += int(i)
    stepa += tsifra ** len(str(chisloo))
    if (int(chisloo) > stepa):
        b = "Число больше"
    if (int(chisloo) < stepa):
        b = "Сумма в сепени больше"
    else:
        b = "ровно"
    return b
print(ahaha(cifri))
