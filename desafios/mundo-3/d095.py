dados, lista, time = {}, [], []
while True:
    dados.clear()
    dados['Nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas o {dados['Nome']} jogou? '))
    lista.clear()
    for p in range(1, partidas + 1):
        lista.append(int(input(f'Quantos gols na {p}° partida? ')))
    dados['Gols'] = lista[:]
    dados['Total'] = sum(lista)
    time.append(dados.copy())
    opção = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if opção in 'N':
        break
print('cod ', end = '')
for i in dados.keys():
    print(f'{i:<15}', end = '')
print()
for c, v in enumerate(time):
    print(f'{c:>4} ', end = '')
    for d in v.values():
        print(f'{str(d):<15}', end = '')
    print()
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! Não existe jogador com número {busca}')
    else:
        print(f'Levantamendo do jogador {time[busca]['Nome']}:')
        for i, g in enumerate(time[busca]['Gols']):
            print(f'No jogo {i + 1} fez {g} gols.')