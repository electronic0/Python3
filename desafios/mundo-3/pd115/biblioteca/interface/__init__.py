def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except ValueError:
            print('Erro. Digite um número inteiro valido.')
        else:
            break
    return num

def linha(tam = 42):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabeçalho('Menu de opções')
    c = 1
    for item in lista:
        print(f'[ {c} ] - {item}')
        c += 1
    print(linha())
    i = leiaInt('Opção: ')
    return i

def cadastro(nome, idade):
    cabeçalho('Novo cadastro')
    with open('desafios/mundo-3/pd115/biblioteca/dados/cadastro.txt', 'a') as file:
        file.write(f'{nome} - {idade} anos \n')

def mostraCadastro():
    cabeçalho('Pessoas cadastradas')
    with open('desafios/mundo-3/pd115/biblioteca/dados/cadastro.txt') as file:
        print(file.read())