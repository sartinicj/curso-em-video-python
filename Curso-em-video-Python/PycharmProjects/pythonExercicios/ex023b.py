'''n = float(input('Digite um numero: '))
print('Numero com 4 digitos a esquerda  = {:04.1f}'.format(n))
print('{4:4f}'.format(n))'''

n = float(input('Digite um numero: '))
print('Numero com 4 digitos a esquerda  = %0 2.0f'%(n))

