con = 0
num = int(input('Digite um numero: '))
for c in range(1, num + 1):
    print(c, end=' ')
    if num % c == 0:
        con += 1
print(f'\nO numero {num} foi divisivel {con} vezes.')
if con == 2:
    print('Por isso ele é um numero PRIMO.')
else:
    print('Por isso ele não é um numero PRIMO.')