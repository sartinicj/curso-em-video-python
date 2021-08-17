import random
pc = random.randint(0, 10)
n = 10
p = 0
while n != pc:
    n = int(input('Pensei em um número de 0 a 10, consegue adivinhar qual foi?'))
    p = p+1
print('É... VOCÊ É BOM, PARA UM HUMANO. Adivinhou depois de {} palpites.'.format(p))

