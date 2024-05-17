sexo = str(input('Qual é o seu genero? [M/F] ')).upper()
while sexo != 'M' and sexo != 'F':
    print('Sexo invalido. Digite novamente')
    sexo = str(input('Qual é o seu genero? [M/F] ')).upper()