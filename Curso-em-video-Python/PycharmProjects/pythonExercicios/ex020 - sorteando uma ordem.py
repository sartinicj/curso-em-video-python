from random import shuffle
print('------- DESAFIO 20 -------')
n1 = (input('Aluno 1: '))
n2 = (input('Aluno 2: '))
n3 = (input('Aluno 3: '))
n4 = (input('Aluno 4: '))
lista = [n1, n2, n3, n4]
nomes = shuffle(lista)
print('A ordem escolhida foi: {}'.format(lista))