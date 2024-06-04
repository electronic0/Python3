l1, l2, l3 = [], [], []
while True:
    n = int(input('Digite um número: '))
    l1.append(n)
    if n % 2 == 0:
        l2.append(n)
    else:
        l3.append(n)
    i = str(input('Deseja continuar [S/N]: ')).upper().strip()
    if i == 'N':
        break
print(f'A lista completa digitada é {l1} \nA lista com somente números pares é {l2} \nA lista com somente números ímpares é {l3}')