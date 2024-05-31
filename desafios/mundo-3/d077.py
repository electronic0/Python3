lista = ('Curso', 'Futuro', 'Aprender', 'Estudar', 'Python', 'Praticar', 'Programador')
for p in lista:
    print(f'\nNa palavra {p} temos', end = ' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end = ' ')