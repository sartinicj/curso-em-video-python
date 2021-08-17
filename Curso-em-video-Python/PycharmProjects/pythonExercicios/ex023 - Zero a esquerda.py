num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('O número digitado foi {}'.format(num))
print('''Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}'''.format(u, d, c, m))
