n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
print('A soma vale {}'.format(n1+n2))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
p = n1**n2
print('A soma vale {}, \n o produto {}, o quosciente {}'.format(s, m, d), end=' ')
print('Divisão exata {}, Potência {}'.format(di, p))
