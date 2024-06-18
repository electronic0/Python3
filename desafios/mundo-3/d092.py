from datetime import date
dados = {}
while True:
    dados['Nome'] = str(input('Digite o nome: ')).strip()
    dados['Idade'] = date.today().year - int(input('Ano de nascimento: '))
    dados['CTPS'] = int(input('Carteira de Trabalho (digite 0 caso não tenha): '))
    if dados['CTPS'] == 0:
        break
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salario'] = float(input('Salario R$'))
    dados['Aposentatoria'] = dados['Idade'] - (date.today().year - dados['Contratação']) + 35
    break
for k, v in dados.items():
    print(f'{k}: {v}')