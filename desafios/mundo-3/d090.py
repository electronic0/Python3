Dados = {}
Nome = str(input('Insira o nome: ')).strip()
Media = float(input(f'Insira a media do {Nome}: '))
Situação = ''
if Media > 6:
    Situação = 'Aprovado'
else:
    Situação = 'Reaprovado'
Dados['Nome'] = Nome
Dados['Media'] = Media
Dados['Situação'] = Situação
for k, v in Dados.items():
    print(f'{k} do aluno é {v}')