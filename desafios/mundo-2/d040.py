n1 = float(input('Digite o valor da primeira nota: '))
n2 = float(input('Digite o valor da segunda nota: '))
m = (n1 + n2) / 2
if m < 5:
    print(f'A media das notas estão abaixo de 5.0. Você está \033[1;31mREPROVADO\033[m \nSua media: {m}')
elif m > 5 and m < 6.9:
    print(f'A media das notas estão entre 5.0 e 6.9. Você está de \033[1;33mRECUPERAÇÃO\033[m \nSua media: {m}')
else:
    print(f'A media das notas estão acima de 7.0. Você está \033[1;32mAPROVADO\033[m \nSua media: {m}')