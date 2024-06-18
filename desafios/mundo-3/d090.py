dados = {}
dados['Nome'] = str(input('Insira o nome: ')).strip()
dados['Media'] = float(input(f'Insira a media do {dados['Nome']}: '))
if dados['Media'] >= 7:
    dados['Situação'] = 'Aprovado'
else:
    dados['Situação'] = 'Reaprovado'
for k, v in dados.items():
    print(f'{k} do aluno é {v}')