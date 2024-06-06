l1 = []
l2 = []
maior = menor = 0
while True:
    l1.append(str(input('Digite o nome: ')))
    l1.append(float(input('Digite o peso: ')))
    if len(l2) == 0:
        maior = menor = l1[1]
    else:
        if l1[1] > maior:
            maior = l1[1]
        elif l1[1] < menor:
            menor = l1[1]
    l2.append(l1[:])
    l1.clear()
    i = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if i in 'N':
        break
print(f'Ao todo foram cadastrados {len(l2)} pessoas. \nO maior peso cadastrado foi {maior}Kg das pessoas', end = ' ')
for p in l2:
    if p[1] == maior:
        print(f'{p[0]}', end = ' ')
print(f'\nE o menor peso cadastrado foi {menor}Kg das pessoas', end = ' ')
for p in l2:
    if p[1] == menor:
        print(f'{p[0]}', end = ' ')