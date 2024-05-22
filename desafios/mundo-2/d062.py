pt = int(input('Digite o valor do primeiro termo: '))
r = int(input('Digite o valor da razão: '))
d = pt + (10 - 1) * r
while d > 0:
    print(d, end = ' ')
    d -= r
    if d <= 0:
        c = int(input('\nQuantos termos que você quer ver mais? '))
        d = pt + (c + 9) * r
        if c == 0:
            d = 0