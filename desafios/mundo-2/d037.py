num = int(input('Digite um número: '))
conv = int(input('Digite um número que corresponde sua base de conversão \n- 1 para binário\n- 2 para octal\n- 3 para hexadecimal\n: '))
if conv == 1:
    print(f'O número {num} convertido para binário fica {bin(num)}')
elif conv == 2:
    print(f'O número {num} convertido para octal fica {oct(num)}')
elif conv == 3:
    print(f'O número {num} convertido para hexadecimal fica {hex(num)}')
else:
    print('Número invalido. Tente novamente.')