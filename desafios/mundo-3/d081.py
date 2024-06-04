lista = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    i = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if i == 'N':
        break  
print(f'Foram digitados {len(lista)} valores na lista. \nA lista ordenada na forma decrescente: {sorted(lista, reverse = True)}')
if lista.count(5) > 0:
    print('O valor 5 está na lista!')
else:
    print('O valor 5 não está na lista.')