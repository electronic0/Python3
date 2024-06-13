dados, lista, qg = {}, [], 0
nome = str(input('Nome do jogador: '))
dados['Nome'] = nome
partidas = int(input(f'Quantas partidas o {nome} jogou? '))
for p in range(1, partidas + 1):
    g = int(input(f'Quantos gols na {p}° partida? '))
    lista.append(g)
    qg += g
dados['Gols'] = lista
dados['Total'] = qg
for k, v in dados.items():
    print(f'{k}: {v}')
print(f'O jogador {nome} jogou {partidas} partidas.')
for p in range(1, partidas + 1):
    print(f'Na {p}° partida, fez {lista[p - 1]} gols')
print(f'Foi um total de {dados['Total']} gols')