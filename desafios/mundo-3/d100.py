from random import randint
from time import sleep
num = []
def sorteia():
    print('Sorteando 5 valores na lista:', end = ' ')
    for n in range(1, 6):
        sleep(0.25)
        na = randint(1, 10)
        print(na, end = ' ')
        num.append(na)
sorteia()
def somaPar():
    soma = 0
    for n in num:
        if n % 2 == 0:
            soma += n
    print(f'\nSomando os valores pares de {num}, temos {soma}')
somaPar()