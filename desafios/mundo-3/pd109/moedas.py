def aumentar(num, p, b):
    if b == True:
        return f'R${num + (num * p / 100):.2f}'
    else:
        return num + (num * p / 100)

def reduzir(num, p, b):
    if b == True:
        return f'R${num - (num * p / 100):.2f}'
    else:    
        return num - (num * p / 100)

def metade(num, b):
    if b == True:
        return f'R${num:.2f}'
    else:
        return num / 2

def dobro(num, b):
    if b == True:
        return f'R${num * 2:.2f}'
    else:
        return num * 2

def moeda(num):
    return f'R${num:.2f}'