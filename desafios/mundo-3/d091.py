from random import randint
from time import sleep
from operator import itemgetter
lista, ranking, lugar = {
    'Jogador 1': randint(1, 6),
    'Jogador 2': randint(1, 6),
    'Jogador 3': randint(1, 6),
    'Jogador 4': randint(1, 6),
}, {}, 0
for c, v in lista.items():
    print(f'{c} sorteou o número {v}')
    sleep(1)
ranking = sorted(lista.items(), key = itemgetter(1), reverse = True)
for c, v in ranking:
    lugar += 1
    print(f'{lugar}º Lugar: {c} com número {v}')
    sleep(1)