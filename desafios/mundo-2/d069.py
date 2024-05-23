maior = homens = mulheres = 0
while True:
    idade = int(input('Digite a ídade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    valor = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if idade > 18:
        maior += 1
    if sexo in 'M':
        homens += 1
    if sexo in 'F' and idade < 20:
        mulheres += 1
    if valor in 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maior} \nHomens que foram cadastrados: {homens} \nMulheres cadastrados abaixo de 20 anos: {mulheres}')