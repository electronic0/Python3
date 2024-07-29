from pd107 import moedas
p = float(input('Digite um preço: R$'))
print(f'Aumentando o preço por 15%, temos R${moedas.aumentar(p, 15):.2f} \nReduzindo o preço por 10%, temos R${moedas.reduzir(p, 10):.2f} \nO dobro de R${p} é R${moedas.dobro(p):.2f} \nA metade de R${p} é R${moedas.metade(p):.2f}')