from math import pow
print('------- DESAFIO 17 -------')
co = float(input('Digite o valor do Cateto Oposto: '))
ca = float(input('Digite o valor do Cateto Adjacente: '))
hip = ((pow(co, 2)) + (pow(ca, 2))) **(1/2)
print('Com CO equivalendo {} e o CA a {} O comprimento da hipotenuza é {}'.format(co, ca, hip))
