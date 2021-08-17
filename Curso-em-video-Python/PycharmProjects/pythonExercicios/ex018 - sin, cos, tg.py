import math
print('------- DESAFIO 18 -------')
a = float(input('Digite o valor de um angulo qualquer: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('Sobre o Ângulo de {} o seno = {:.2f} O cosseno = {:.2f} e a tangente = {:.2f}'.format(a, s, c, t))
