from random import randint
cnum = randint(0, 5)
print('Eu (computador) escolhi um número aleatório entre 0 a 5.')
num = int(input('Qual número que eu escolhi? '))
if num == cnum:
    print(f'Parabens! Você acertou o número que eu escolhi, que no caso é o {cnum}')
else:
    print(f'Errou! Você errou o número que eu escolhi. Eu escolhi o número {cnum}')