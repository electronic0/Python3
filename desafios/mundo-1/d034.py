s = float(input('Qual é o salario do funcionario? R$'))
if s >= 1250:
    print(f'O salario do funcionario esta acima de R$1250. Com isso, vai receber um aumento de 10% que fica no valor de R${s + (s * 10 / 100):.2f}')
else:
    print(f'O salario do funcionario esta abaixo de R$1250. Com isso, vai receber um aumento de 15% que fica no valor de R${s + (s * 15 / 100):.2f}')