print('Para imprimir na tela um texto longo basta colocar três aspas simples no print:')
print('''Welcome! Are you completely new to programing?
about why and how to get started with Python. Fortunately
an experienced programmer in any programming language
(whatever it may be) can pick up Python very quickly.
Its so easy for begginers to use and learn, so jump in!''')
frase = 'Curso em Vídeo Pyhthon'
print()
print('Impressão simples na tela, da frase:')
print(frase)
print()
print('Impressão na tela, da letra no posição [3]:')
print(frase[3])
print()
print('Impressão na tela, do conteúdo entre posição [3 até 13]:')
print(frase[3:13])
print()
print('Impressão na tela, do conteúdo do início até a posição [13]:')
print(frase[:13])
print()
print('Impressão na tela, do conteúdo da posição [13] até o final:')
print(frase[13:])
print()
print('Impressão na tela, do conteúdo entre posição [1 até 15] pulando duas vezes:')
print(frase[1:15:2])
print()
print('Impressão na tela, do conteúdo do início ao fim pulando duas vezes:')
print(frase[::2])
print()
print('Impressão na tela, da contagem de aparições da letra o:')
print(frase.count('o'))
print()
print('Impressão na tela, da contagem de aparições da letra O:')
print(frase.count('O'))
print()
print('Impressão na tela, da contagem de aparções da letra O, após colocar tudo em maiúscula:')
print(frase.upper().count('O'))
print()
print('Impressão na tela, da contagem de caracteres:')
print(len(frase))
print()
frase = '       Curso em Vídeo Pyhthon    '
print(frase)
print('Impressão na tela, da contagem de caracteres com espaços:')
print(len(frase))
print('Impressão na tela, da contagem de caracteres sem espaços:')
print(len(frase.strip()))
print()
frase = 'Curso em Vídeo Pyhthon'
print('Impressão na tela, da substituição de Python por Android na memória:')
frase = frase.replace('Python', 'Android')
print('frase = frase.replace(Python, Android)')
print()
print('Impressão na tela, de verificação se existe a palavra Curso:')
print('Curso' in frase)
print()
print('Impressão na tela, da verificação da posição inicial da palavra Curso:')
print(frase.find('Curso'))
print()
print('Impressão na tela, da verificação da posição da palavra curso:')
print(frase.find('curso'))
print()
print('Impressão na tela, da frase dividida:')
print(frase.split())
dividido = frase.split()
#print(dividido)
print()
print('Impressão na tela, da frase dividida na posição [0]:')
print(dividido[0])
print()
print('Impressão na tela, da frase dividida na posição [0] com a letra da posição [2]:')
print(dividido[0][2])
