n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'trêze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    v = int(input('Digite um número entre 0 a 20: '))
    if v >= 0 and v <= 20:
        break
    else:
        print('Tente novamente.', end = ' ')
print(f'Você digitou o número {n[v]}')