from datetime import date
ano = int(input('Que ano você nasceu? '))
idade = date.today().year - ano
if idade < 18:
    print(f'Falta {18 - idade} anos para se alistar ao serviço militar.')
elif idade == 18:
    print('Já esta na hora de se alistar ao serviço militar.')
else:
    print(f'Já passou o prazo de {idade - 18} anos de alistamento militar.')