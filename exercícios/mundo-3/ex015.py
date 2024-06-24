def soma(* val):
    s = 0
    for num in val:
        s += num
    print(f'Somando os valores {val} temos {s}')
soma(5, 2, 3)
soma(9, 8, 2, 4, 3)