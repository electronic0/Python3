dados, lista = {}, []
dados['Nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas o {dados['Nome']} jogou? '))
for p in range(1, partidas + 1):
    lista.append(int(input(f'Quantos gols na {p}° partida? ')))
dados['Gols'] = lista
dados['Total'] = sum(lista)
for c, v in dados.items():
    print(f'{c}: {v}')
print(f'O jogador {dados['Nome']} jogou {partidas} partidas.')
for p in range(1, partidas + 1):
    print(f'Na {p}° partida, fez {lista[p - 1]} gols')
print(f'Foi um total de {dados['Total']} gols')