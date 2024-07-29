def moeda(num):
    return f'R${num:.2f}'

def resumo(num, a, r):
    print(f'Preço analisado: {moeda(num)} \nDobro do preço: {moeda(num * 2)} \nMetade do preço: {moeda(num / 2)} \n{a}% de aumento: {moeda(num + (num * a / 100))} \n{r}% de redução: {moeda(num - (num * r / 100))}')
