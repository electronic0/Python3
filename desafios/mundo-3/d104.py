def leiaInt(msg):
    while True:
        num = input(msg)
        if num.isnumeric():
            break
        else:
            print('Erro! Digite um número inteiro válido')
    return num
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')