a = 0
for i in range(1, 1001):
    u = str(i)
    if u[::-1] == str(i):
        a += 1
print(a)