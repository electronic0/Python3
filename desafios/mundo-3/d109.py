from pd109 import moedas
p = float(input('Digite um preço: R$'))
print(f'Aumentando o preço por 15%, temos {moedas.aumentar(p, 15, True)} \nReduzindo o preço por 10%, temos {moedas.reduzir(p, 10, True)} \nO dobro de {moedas.moeda(p)} é {moedas.dobro(p, True)} \nA metade de {moedas.moeda(p)} é {moedas.metade(p, False)}')