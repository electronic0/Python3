n = int(input('Digite um número: '))
n1 = 0
n2 = 1
v = 0
print(f'{n1} {n2}', end = ' ')
while v < n:
    n3 = n1 + n2
    print(n3, end = ' ')
    v += 1
    n1 = n2
    n2 = n3