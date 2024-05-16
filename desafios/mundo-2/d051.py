pt = int(input('Digite o valor do primeiro termo: '))
r = int(input('Digite um valor da razão: '))
d = pt + (10 - 1) * r
for c in range(pt, d + r, r):
    print(c)
