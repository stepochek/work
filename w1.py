import random
d = ''
m = 0
file = open('lol.txt').readlines()
fule = open('lol.txt', 'w')
for i in file:
    g = i .split(' ')
    n = random.randint(1,len(g) - 1)
    for h in g[n]:
        d += h
        for y in g:
            if d in y:
                m += 1
            else:
                fule.write(y)
fule.close()

