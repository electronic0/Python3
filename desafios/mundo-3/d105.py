def notas(* notas, sit = False):
    lista = {
        'Total': len(notas),
        'Maior': max(notas),
        'Menor': min(notas),
        'Média': sum(notas) / len(notas)
    }
    if sit == True:
        if lista['Média'] < 6:
            lista['Situação'] = 'Ruim'
        elif lista['Média'] < 7:
            lista['Situação'] = 'Razoavel'
        elif lista['Média'] >= 7:
            lista['Situação'] = 'Boa'
    return print(lista)
notas(5.5, 9.5, 10, 6.5, sit = False)