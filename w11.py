answ = 0
for i in range(10, 1000):
    if i < 100:
        xren = i % 10 + i % 100 // 10
        if xren % 2 == 0:
            answ += i
    else:
        xren2 = i % 10 + i % 100 // 10 + i % 1000 // 100
        if xren2 % 2 == 0:
            answ += i
print(answ)
