import requests
try:
    site = requests.get('https://www.google.com.br/?hl=pt-BR')
except Exception as erro:
    print('Site não acessivel')
else:
    print('Site acessivel')