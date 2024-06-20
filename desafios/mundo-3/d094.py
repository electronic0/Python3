lista, dados = {}, []
soma = media = 0
while True:
    lista['Nome'] = str(input('Digite o nome: '))
    while True:
        lista['Sexo'] = str(input('Digite o gênero: ')).upper().strip()[0]
        if lista['Sexo'] in 'MF':
            break
        print('Erro! Tente novamente')
    lista['Idade'] = int(input('Digite a idade: '))
    soma += lista['Idade']
    dados.append(lista.copy())
    opção = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if opção in 'N':
        break
print(f'Ao todo temos {len(dados)} pessoas cadastradas. \nA média das idades cadastradas é {soma / len(dados):5.2f} \nAs mulheres cadastradas:', end = ' ')
for p in dados:
    if p['Sexo'] in 'F':
        print(f'{p['Nome']}', end = ' ')
