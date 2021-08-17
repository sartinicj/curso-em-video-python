nome = input('Digite seu nome completo: ')
div = nome.split()
print('O nome inserido foi [{}].'.format(nome))
print('O primeiro nome digitado foi {}.'.format(div[0]))
print('O último nome digitado foi {}'.format(nome[len(nome)-1]))

