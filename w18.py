deneg = int(input(':'))
procent = int(input(':'))
dney = int(input(':'))
procentvden = procent / 365
for i in range(dney):
    deneg += deneg / 100 * procentvden
print(deneg)