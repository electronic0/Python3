from random import choice
a1 = input('Qual é o nome do primeiro aluno? ')
a2 = input('Qual é o nome do segundo aluno? ')
a3 = input('Qual é o nome do terceiro aluno? ')
a4 = input('Qual é o nome do quarto aluno? ')
escolhido = choice([a1, a2, a3, a4])
print(f'O aluno {escolhido} foi escolhido para apagar o quadro do professor.')
