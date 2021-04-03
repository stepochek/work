gramms = int(input("gramms"))
years = int(input('years')) * 365
procent = int(input("procent"))
for i in range(years):
    pribily = gramms / 100 * procent / 365
    gramms = gramms + pribily
print(gramms)