c1 = float(input('Digite o primeiro valor do comprimento: '))
c2 = float(input('Digite o segundo valor do comprimento: '))
c3 = float(input('Digite o terceiro valor do comprimento: '))
if c1 < c2 + c3 and c2 < c1 + c3 and c3 < c1 + c2:
    print(f'Com base nos valores dado, é possivel formar um triangulo!')
else:
    print(f'Com base nos valores dado, não é possivel formar um triangulo, pois um lado do comprimento esta maior ou menor do que os outros.')