n1 = input('Digite o primeiro numero: ')
n2 = input('Digite o segundo numero: ')
n3 = input('Digite o terceiro numero: ')
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'O menor numero entre os três é o {menor} e o maior numero entre os três é o {maior}')