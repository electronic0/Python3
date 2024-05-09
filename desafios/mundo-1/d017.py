from math import hypot
co = float(input('Qual é o comprimento do cateto oposto? '))
ca = float(input('Qual é o comprimento do cateto adjacente? '))
h = hypot(co, ca)
print(f'O comprimento da hipotenusa de um triângulo retângulo é {h:.2f}')