from random import choice
com = choice(['Pedra', 'Papel', 'Tesoura'])
jog = str(input('Bora jogar Pedra Papel e Tesoura? Escolhe qual mão que vai jogar: ')).capitalize()
if com == 'Pedra' and jog == 'Tesoura' or com == 'Papel' and jog == 'Pedra' or com == 'Tesoura' and jog == 'Papel':
    print('Computador venceu!')
elif jog == 'Pedra' and com == 'Tesoura' or jog == 'Papel' and com == 'Pedra' or jog == 'Tesoura' and com == 'Papel':
    print('Você venceu!')
else:
    print('Empate!')