n = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')),
int(input('Digite o último número: ')))
print(f'Voce digitou os números {n} \nO valor 9 apareceu {n.count(9)} vezes\nOs valores pares digitados foram ', end = '')
for i in n:
    if i % 2 == 0:
        print(i, end = ' ')
if 3 in n:
    print(f'\nO valor 3 apareceu na {lista.n(3) + 1}° posição da lista ')
else:
    print('\nO valor 3 não esta na lista')