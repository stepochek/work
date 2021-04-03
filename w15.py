primer = input('primer:')
def my(prime):
    print(prime)
    ind = 2
    answ = 0
    for i in range(len(prime)):
        if prime[ind] == '+':
            answ1 = int(prime[ind - 1]) + int(prime[ind + 1])
            answ += answ1
            ind += 2
            print('lol')
        elif primer[ind] == '-':
            answ2 = prime[ind - 1] - prime[ind + 1]
            answ += answ2
            ind += 2
            print('lol1')
        elif prime[ind] == '%':
            answ3 = prime[ind - 1] % prime[ind + 1]
            answ += answ3
            ind += 2
            print('lol2')
        elif prime[ind] == '/':
            answ4 = prime[ind - 1] / prime[ind + 1]
            answ += answ4
            ind += 2
            print('lol3')
        elif prime[ind] == '//':
            answ5 = prime[ind - 1] // prime[ind + 1]
            answ += answ5
            ind += 2
            print('lol4')
    return answ
print(my(primer))