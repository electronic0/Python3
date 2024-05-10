cidade = str(input('Digite um nome de uma cidade: '))
santo = cidade.split()[0].upper()
print(f'O nome da cidade começa com a palavra Santo? {'SANTO' in santo}')