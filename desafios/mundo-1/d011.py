l = float(input('Qual é a largura da sua parede em metros? '))
a = float(input('Qual é altura da sua parede em metros? '))
area = l * a
print(f'Com base dos valores dado, sua area é {area:.2f}m² \nPara pintar as paredes, é necessario usar {area / 2:.2f} litros de tinta.')