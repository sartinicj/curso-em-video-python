nome = str(input('Qual seu nome? '))
if nome == 'Cecilia':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo' :
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Claudia Jéssica Juliana':
    print('Belo nome feminino.')
else:
    print('Que nome comum.')
print('Tenha um bom dia, {}! '.format(nome))