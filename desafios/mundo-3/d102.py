def fatorial(num = 1, show = False):
    f = 1
    for n in range(num, 0, -1):
        f *= n
    if show == True:
        while num > 0:
            print(f'{num}', end = ' ')
            print('x ' if num > 1 else '= ', end = '')
            num -= 1
    return f

print(fatorial(5, show=True))