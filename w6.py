a = input('')
def season(g):
    if int(g) >= 3 and int(g) <= 5:
        d = 'веснa'
        return d
    elif int(g) >= 6 and int(g) <= 8:
        d = 'лето'
        return d
    elif int(g) >= 9 and int(g) <= 11:
        d = 'осень'
        return d
    else:
        d = 'зима'
        return d
print(season(a))
