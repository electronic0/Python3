cidade = str(input('Digite um nome de uma cidade: '))
print(f'O nome da cidade começa com a palavra Santo? {cidade.split()[0].upper() == 'SANTO'}')