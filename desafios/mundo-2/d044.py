preço = float(input('Qual é o preço do produto? R$'))
cond = int(input('Formas de pagamento \n1 - à vista dinheiro/cheque\n2 - à vista no cartão\n3 - 2x no cartão\n4 - 3x ou mais no cartão\nQual vai ser a opção? '))
if cond == 1:
    print(f'Sua compra de R${preço:.2f} vai custar R${preço - (preço * 10 / 100):.2f}')
elif cond == 2:
    print(f'Sua compra de R${preço:.2f} vai custar R${preço - (preço * 5 / 100):.2f}')
elif cond == 3:
    print(f'Sua compra será parcelada em 2x de R${preço / 2:.2f} sem juros. \nSua compra vai custar R${preço}')
else:
    par = int(input('Quantas parcelas? '))
    print(f'Sua compra será parcelada em {par}x de R${(preço / par) + ((preço / par) * 20 / 100):.2f} com juros. \nSua compra de R${preço} vai custar R${preço + (preço * 20 / 100):.2f}')