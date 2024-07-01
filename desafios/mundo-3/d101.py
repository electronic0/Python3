from datetime import date
nas = int(input('Em que ano você nasceu? '))
idade = date.today().year - nas
def voto(nasc):
    if idade < 18:
        return 'Não vota'
    elif idade < 65:
        return 'Voto obrigatorio'
    else:
        return 'Voto opcional'
print(f'Com {idade} anos: {voto(nas)}')