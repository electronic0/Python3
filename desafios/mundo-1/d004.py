valor = input('Digite um valor qualquer: ')
print(f'O tipo do valor: {type(valor)} \nEle é numero? {valor.isnumeric()} \nEle é uma letra? {valor.isalpha()} \nEle é alfanumerico? {valor.isalnum()}')