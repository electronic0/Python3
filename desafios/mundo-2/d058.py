from random import randint
c = randint(0, 10)
p = 0
esc = int(input('Eu escolhi um número entre 0 a 10. Qual numero eu escolhi? '))
while esc != c:
    p += 1
    esc = int(input('Errou, tente novamente: '))
print(f'Parabens você ganhou! Você fez no minino {p} palpites para acertar a resposta.')