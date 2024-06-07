matriz = [[], [], []]
s = stc = 0
for y in range(0, 3):
    for x in range(0, 3):
        n = int(input(f'Digite um valor para a posição {y, x}: '))
        matriz[y].append(n)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[ {matriz[l][c]} ]', end = ' ')
        if matriz[l][c] % 2 == 0:
            s += matriz[l][c]
    stc += matriz[l][2]
    print()
print(f'A soma dos valores pares digitados é {s}. \nA soma dos valores na terceira coluna é {stc}. \nO maior valor da segunda linha é {max(matriz[1])}')