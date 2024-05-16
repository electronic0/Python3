from datetime import date
maiores, menores = 0, 0
for c in range(1, 8):
    nas = int(input('Ano de nascimento: '))
    idade = date.today().year - nas
    if idade >= 21:
        maiores += 1
    else:
        menores += 1
print(f'O numero de pessoas que são da maioridade é {maiores}, e o numero de pessoas que são da menoridade é {menores}.')