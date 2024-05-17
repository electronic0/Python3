maioridade, soma, qua = 0, 0, 0
velho = ''
for p in range(1, 5):
    nome = str(input('Digite o nome: ')).strip()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o seu genero: ')).capitalize().strip()
    if p == 1 and sexo == 'Masculino':
        maioridade = idade
        velho = nome
    if sexo == 'Masculino' and idade > maioridade:
        maioridade = idade
        velho = nome
    if sexo == 'Feminino' and idade < 20:
        qua += 1
    soma += idade
media = soma / 4
print(f'A media de idade do grupo: {media} Anos. \nO nome da pessoa mais velho {velho} \nA quantidade de mulheres que tem menos de 20 anos é {qua}')