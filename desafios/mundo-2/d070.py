gasto = quantidade = barato = menor = 0
while True:
    nome = str(input('Nome do produto: ')).strip()
    preço = float(input('Preço do produto R$'))
    valor = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    gasto += preço
    barato += 1
    if barato == 1:
        menor = preço
    else:
        if preço < menor:
            menor = preço
    if preço > 1000:
        quantidade += 1
    if valor in 'N':
        break
print(f'O gasto total da compra foi R${gasto:.2f} \nTem {quantidade} produtos que custam acima de R$1000.00 \nO produto mais barato custa R${barato:.2f}')