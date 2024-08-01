from pd115.biblioteca.interface import *

while True:
    resp = menu(['Ver pessoas cadastradas no sistema', 'Cadastrar uma nova pessoa no sistema', 'Sair do sistema'])
    if resp == 1:
        mostraCadastro()
    elif resp == 2:
        while True:
            try:
                nome = str(input('Nome da pessoa: ')).strip()
                idade = int(input('Idade da pessoa: '))
            except (ValueError, TypeError):
                print('Ocorreu um erro durante o cadastro. Tente novamente')
            else:
                cadastro(nome, idade)
                print(f'Novo cadastro de {nome} registrado com sucesso!')
                break
    elif resp == 3:
        print('Saindo do sistema. Volte sempre')
        break
    else:
        print('Erro. Opção invalida')