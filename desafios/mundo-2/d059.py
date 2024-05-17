n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
v = 0
while v != 5:
    v = int(input('O que você deseja? \n[1] - Somar os números \n[2] - Multiplicar os números \n[3] - Saber qual é o maior valor \n[4] - Digitar novos números \n[5] - Sair do programa \nOpção: '))
    if v == 1:
        print(f'A soma dos números é igual a {n1 + n2}')
    elif v == 2:
        print(f'A multplicação dos número é igual a {n1 * n2}')
    elif v == 3:
        if n1 > n2:
            print(f'O primeiro valor {n1} é maior que {n2}')
        else:
            print(f'O segundo valor {n2} é maior que {n1}')
    elif v == 4:
        n1 = float(input('Digite um valor: '))
        n2 = float(input('Digite outro valor: '))