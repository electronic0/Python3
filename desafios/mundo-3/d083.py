e = str(input('Digite a expressão matematica: '))
lista = []
for s in e:
    if s == '(':
        lista.append('(')
    elif s == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            pilha.append(')')
            break
if len(lista) == 0:
    print('Sua expressão está valida!')
else:
    print('Sua expressão não é valida!')