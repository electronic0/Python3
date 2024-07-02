from time import sleep
print('Sistema de Ajuda PyHelp')
while True:
    i = str(input('Digite uma função ou biblioteca: ')).strip()
    sleep(1)
    if i in 'fim':
        break
    print(f"Acessando o manual do comando '{i}'")
    sleep(1)
    help(i)
print('Volte sempre!')