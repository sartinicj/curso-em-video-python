'''for i in range(1, 10):
    print(i)
print('`~´'*20)
print('FIM')'''
i = 1
while i < 10:
    print(i)
    i = i+1
print('`~´'*20)
'''for i in range(1, 5):
    n = int(input('Digite um valor: '))
print('`~´'*20)
print('FIM')
print('`~´'*20)'''
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('`~´' * 20)
print('FIM')
print('`~´' * 20)
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar?[S/N]: ')).upper()
print('FIM')
print('`~´' * 20)
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar +=1
print('Você digitou {} números pares e {} ímpares!'.format(par, impar))

