def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except ValueError:
            print('Erro. Digite um número inteiro valido.')
        else:
            break
    return num

def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except ValueError:
            print('Erro. Digite um número real valido.')
        else:
            break
    return num

n = leiaInt('Digite um número inteiro: ')
r = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {n} e o real foi {r}')