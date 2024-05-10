vel = int(input('Qual é a velocidade do carro no momento? '))
multa = 7 * (vel - 80)
if vel > 80:
    print(f'Você foi multado por ultrapassar na velocidade de 80Km/h. A multa vai custar R${multa}')
else:
    print('Obrigado por respeitar as leis de trânsito! Você esta na velocidade abaixo de 80Km/h')
