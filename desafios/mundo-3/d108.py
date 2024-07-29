from pd108 import moedas
p = float(input('Digite um preço: R$'))
print(f'Aumentando o preço por 15%, temos {moedas.moeda(moedas.aumentar(p, 15))} \nReduzindo o preço por 10%, temos {moedas.moeda(moedas.reduzir(p, 10))} \nO dobro de {moedas.moeda(p)} é {moedas.moeda(moedas.dobro(p))} \nA metade de {moedas.moeda(p)} é {moedas.moeda(moedas.metade(p))}')