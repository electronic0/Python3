d = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos Km rodados até no momento? '))
preço = 60 * d +  0.15 * km
print(f'O preço do carro alugado a pagar vai ser R${preço:.2f}')