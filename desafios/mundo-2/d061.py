pt = int(input('Digite o valor do primeiro termo: '))
r = int(input('Digite o valor da razão: '))
d = pt + (10 - 1) * r
while d >= 0:
    print(d, end = ' ')
    d -= r