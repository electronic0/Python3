from datetime import date
ano = int(input('Qual é seu ano de nascimento? '))
idade = date.today().year - ano
if idade <= 9:
    print(f'O atleta de {idade} anos está na categoria Mirim')
elif idade > 9 and idade <= 14:
    print(f'O atleta de {idade} anos está na categoria Infantil')
elif idade > 14 and idade <= 19:
    print(f'O atleta de {idade} anos está na categoria Junior')
elif idade > 19 and idade <= 20:
    print(f'O atleta de {idade} anos está na categoria Sênior')
else:
    print(f'O atleta de {idade} anos está na categoria Master')