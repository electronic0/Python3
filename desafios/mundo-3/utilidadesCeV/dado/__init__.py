def leiaDinheiro(txt):
    while True:
        num = str(input(f'{txt}')).strip()
        if num.isalpha() or len(num) == 0:
            print('Erro. Digite o preço novamente')
        else:
            return float(num)