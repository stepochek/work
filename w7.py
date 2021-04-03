a = input('pro')
b = ['t']
def arg(a, b):
    answ = 0
    n = ''
    for y in b:
        n += y
    for i in a:
        if n in i:
            answ += 1
    return answ
print(arg(a ,b))
