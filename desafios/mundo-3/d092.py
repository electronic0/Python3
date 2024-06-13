from datetime import date
dados = {}
while True:
    nome = str(input('Digite o nome: ')).strip()
    dados['Nome'] = nome
    nascimento = date.today().year - int(input('Ano de nascimento: '))
    dados['Idade'] = nascimento
    ctps = int(input('Carteira de Trabalho (digite 0 caos não tenha): '))
    dados['CTPS'] = ctps
    if ctps == 0:
        break
    contratacao = int(input('Ano de contratação: '))
    dados['Contratação'] = contratacao
    salario = float(input('Salario R$'))
    dados['Salario'] = salario
    break
dados['Aposentatoria'] = nascimento - (date.today().year - contratacao) + 35
for k, v in dados.items():
    print(f'{k}: {v}')