v = int(input('Qual valor deseja sacar? R$'))
c, ced = 0, 50
while True:
    if v >= ced:
        v -= ced
        c += 1
    else:
        if c > 0:
            print(f'{c} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        c = 0
        if v == 0:
            break