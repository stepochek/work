n = 0
with open('lol.txt','r') as file:
    for i in file:
        for j in i:
            if j.isdigit() and not int(j ) %2 != 0:
                n += int(j)
print(n)
