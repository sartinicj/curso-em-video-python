import random
n = int(input('Pensei em um número de 0 a 5, consegue adivinhar qual foi?'))
pc = random.randint(0, 5)
print('É... VOCÊ É BOM, PARA UM HUMANO.' if n == pc else 'MUAHAHAHA VOCÊ NUNCA VAI ACERTAR!!!')


