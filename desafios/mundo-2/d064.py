v = c = s = 0
while v != 999:
    n = int(input('Digite um número (digite o valor 999 caso quer que o programa pare): '))
    if n != 999:
        c += 1
        s = n + s
    v = n
print(f'Foram digitados {c} valores que, ao somar ao todo, fica no valor de {s}')