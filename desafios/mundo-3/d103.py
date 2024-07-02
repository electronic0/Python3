def ficha(nome = 'desconhecido', gols = 0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')
nome = str(input('Digite o nome do jogador: ')).strip()
gols = input('Digite o número de gols: ')
if nome in '':
    nome = 'desconhecido'
if gols in '':
    gols = 0
ficha(nome, gols)