nome = input('Digite seu nome completo:')
div = nome.split()
ce = len(nome)
print('O nome digitado foi: {}'.format(nome))
print('O nome digitado com as letras maíúsculas será: {}'.format(nome.upper()))
print('O nome digitado com as letras minúsculas será: {}'.format(nome.lower()))
print('O nome {} sem espaço, tem a seguinte quantia de letras: {}'.format(nome, len(nome.replace(" ", ""))))
print('O primeiro nome digitado {} tem a seguinte quatia de letras: {} '.format(div[0], len(div[0])))




