soma = 0
for c in range(1, 7):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        soma += valor
print(f'A soma dos valores digitados em pares fica {soma}')