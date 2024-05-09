from random import sample
a1 = input('Coloque o nome do primeiro aluno: ')
a2 = input('Coloque o nome do segundo aluno: ')
a3 = input('Coloque o nome do terceiro aluno: ')
a4 = input('Coloque o nome do quarto aluno: ')
esc = sample([a1, a2, a3, a4], k = 4)
print(f'A ordem de apresentação dos trabalhos vai ser {esc}')