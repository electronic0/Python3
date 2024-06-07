from random import randint
from time import sleep
print('JOGA NA MEGA SENA')
q = int(input('Quantos jogos você quer que eu sorteie? '))
for j in range(1, q + 1):
    lista = [randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60)]
    print(f'Jogo {j}: {sorted(lista)}')
    sleep(1)
print('Boa sorte!')