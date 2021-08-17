from datetime import date
ano = int(input('Digite o ano do seu nascimento: '))
m = ano+18
if m > date.today().year:
    a = m - date.today().year
    print('Ainda não é tempo de se alistar. Faltam {} anos.'.format(a))
elif m < date.today().year:
    a = date.today().year - m
    print('Já passou do tempo de se alistar. Deveria ter se alistado ha {} anos atrás'.format(a))
else:
    print('É O ANO DE SE ALISTAR!')


