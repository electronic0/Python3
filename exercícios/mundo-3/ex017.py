try:
    num = int(input('Digite um número: '))
except Exception as erro:
    print(f'Tivemos problemas com os tipos de dados {erro.__cause__}')
else:
    print(f'Você digitou o número {num}')
finally:
    print(f'Volte sempre')