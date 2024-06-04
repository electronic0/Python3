lista = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if lista.count(n) > 1:
        print('Número duplicado. Não foi registrado')
        lista.remove(n)
    else:
        print('Número registrado com sucesso.')
    i = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if i == 'N':
        break
print(f'Você digitou os valores {sorted(lista)}')