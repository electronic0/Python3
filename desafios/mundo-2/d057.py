sexo = str(input('Qual é o seu genero? [M/F] ')).upper().strip()
while sexo != 'M' and sexo != 'F':
    print('Sexo invalido. Digite novamente')
    sexo = str(input('Qual é o seu genero? [M/F] ')).upper().strip()
print('Registrado com sucesso!')