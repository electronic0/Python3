matriz = [[], [], []]
for y in range(0, 3):
    for x in range(0, 3):
        n = int(input(f'Digite um valor para posição {y, x}: '))
        matriz[y].append(n)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[ {matriz[l][c]} ]', end = ' ')
    print()