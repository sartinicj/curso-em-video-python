n1 = input('Digite o primeiro valor: ')
print(type(n1))
n2 = int(input('Qual o primeiro número?'))
print(type(n2))
pnum = input('Qual o primeiro número?')
snum = input('Qual o segundo número?')
sum = pnum+snum
print('A concatenação é ', sum)
pnum = int(input('Qual o primeiro número?'))
snum = int(input('Qual o segundo número?'))
sum = pnum+snum
print('A soma de', pnum, ' com ', snum, ' é igual a ', sum)
print('Com o uso da máscara, o print fica mais bonito no código:')
print('A soma de {} com {} é igual a {}'.format(pnum, snum, sum))
