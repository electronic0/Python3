from time import sleep
def contador(inicio, fim, passo):
    if inicio > fim:
        fim -= passo
        passo = -passo
    for n in range(inicio, fim, passo):
        print(n, end = ' ')
        sleep(0.25)
    print('Fim!')
print('Contagem de 1 até 10 de 1 em 1')
sleep(1)
contador(1, 11, 1)
print('Contagem de 10 até 0 de 2 em 2')
sleep(1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
if p == 0:
    p = 1
if p < 0:
    p *= -1
print(f'Contagem de {i} até {f} de {p} em {p}')
contador(i, f, p)