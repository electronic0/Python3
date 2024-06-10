lista = []
while True:
    nome = str(input('Digite o nome: ')).strip()
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    media = (n1 + n2) / 2
    lista.append([nome, [n1, n2], media])
    i = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if i == 'N':
        break
print(f'{'No.':<4}{'Nome':<10}{'Media':<20}')
for n, p in enumerate(lista):
    print(f'{n:<4}{p[0]:<10}{p[2]:<20.1f}')
while True:
    op = int(input('Mostrar notas de qual aluno? (digite 999 caso queria parar): '))
    if op == 999:
        break
    if op <= len(lista) - 1:
        print(f'Notas de {lista[op][0]} são {lista[op][1]}')