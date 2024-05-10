n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print(f'A sua media foi {m:.1f}')
if m >= 6:
    print('Sua media foi boa. Parabens!')
else:
    print('Sua media foi ruim. Estude mais!')