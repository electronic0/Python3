from math import radians, sin, cos, tan
ang = float(input('Digite um angulo: °'))
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))
print(f'O seno de {ang}° é {seno:.2f} \nO cosseno de {ang}° é {cosseno:.2f} \nA tangente de {ang}° é {tangente:.2f}')