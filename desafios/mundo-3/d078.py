vlrs = []
for v in range(0, 5):
    vlrs.append(int(input(f'Digite um número para a posição {v}: ')))
print(f'O maior número digitado foi {max(vlrs)} e está na posição {vlrs.index(max(vlrs))} \nO menor número digitado foi {min(vlrs)} e está na posição {vlrs.index(min(vlrs))}')