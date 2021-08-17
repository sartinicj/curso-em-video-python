'''import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} arredondada para cima é igual a {}'.format(num, math.ceil(raiz)))
print('A raiz de {} arredondada para baixo é igual a {}'.format(num, math.floor(raiz)))
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))
from math import sqrt
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))'''
from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, floor(raiz)))


