lista = []
for v in range(0, 5):
    n = int(input('Digite um número: '))
    if v == 0 or n > lista[len(lista) - 1]:
        lista.append(n) 
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print(f'Os valores digitados em ordem é {lista}')