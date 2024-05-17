n = int(input('Digite um numero: '))
c, s = 0, 0
while n != 999:
    n = int(input('Digite um valor qualquer (se digitar o valor 999 o programa para): '))
    if n != 999:
        c += 1
        s = n + s
print(f'Foram digitados {c} valores que, ao somar os números, dá o resultado de {s}')