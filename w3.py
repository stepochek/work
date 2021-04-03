import random
file = input('Edit text:')
fule = []
fuller = []
fule.append(file)
for i in fule:
    f = i.split(' ')
    print(f)
    for h in f:
        n = random.randint(0,len(f))
        if h not in fuller:
            fuller.append(f[n - 1])
print(fuller)
