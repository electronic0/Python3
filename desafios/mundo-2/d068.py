from random import randint
print('Vamos jogar par ou ímpar?')
q = 0
while True:
    n = int(input('Digite um número: '))
    v = str(input('Par ou ímpar? ')).strip().upper()
    c = randint(1, 100)
    print(f'Você jogou {n} e o computador {c}. A soma vale {n + c}.')
    if v in 'PARP' and (n + c) % 2 == 0:
        print('Você venceu. \nVamos jogar novamente.')
        q += 1
    elif v in 'ÍMPARIÍ' and (n + c) % 2 == 1:
        print('Você venceu. \nVamos jogar novamente.')
        q += 1
    else:
        break
print(f'Voce perdeu. Você venceu {q} vezes')