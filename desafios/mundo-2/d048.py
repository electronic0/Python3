s, con = 0, 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        con += 1
print(f'A soma de {con} valores solicitados é {s}')