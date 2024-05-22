s = 'S'
q = soma = m = maior = menor = 0
while s != 'N':
    n = int(input('Digite um número: '))
    q += 1
    soma += n
    if q == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    s = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    m = soma / q
print(f'Voce digitou {q} valores e a media entre eles é {m:.2f} \nO maior número digitado foi o {maior} e o menor número digitado foi {menor}')