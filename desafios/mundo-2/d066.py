s = c = 0
while True:
    n = int(input('Digite um número: (escreva 999 caso queria parar) '))
    if n == 999:
        break
    s += n
    c += 1
print(f'Foram digitados {c} valores. A soma vale {s}')