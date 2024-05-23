s = 0
while True:
    n = int(input('Digite um número: (escreva 999 caso queria parar) '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')