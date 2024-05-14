casa = float(input('Qual é o valor da casa? R$'))
salario = float(input('Qual é o salario do comprador? R$'))
anos = int(input('Quantos anos de pagamento? '))
valor = casa / (12 * anos)
print(f'Para pagar a casa de R${casa:.2f} em {anos} anos será necessario pagar a prestação de R${valor:.2f}')
if valor > (salario * 30 / 100):
    print(f'Emprestimo \033[1;31mNegado\033[m')
else:
    print(f'Emprestimo \033[1;32mAprovado\033[m')