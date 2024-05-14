peso = float(input('Qual é o seu peso? '))
altura = float(input('Qual é sua altura? '))
imc = peso / pow(altura, 2)
if imc <= 18.5:
    print('Você esta abaixo do peso.')
elif imc > 18.5 and imc <= 25:
    print('Você esta no peso ideal.')
elif imc > 25 and imc <= 30:
    print('Você esta sobrepeso.')
elif imc > 30 and imc <= 40:
    print('Você esta na obesidade.')
else:
    print('Você esta na obesidade mórbida.')
