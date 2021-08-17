'''
print( )
print('DESAFIO 1')
nome = input ('Qual seu nome?')
print('Ola ' +nome+ ' Seja bem vindx!')
print( )
print('------- DESAFIO 02 -------')
dia = input ('Qual o dia que você nasceu?')
mes = input ('Qual o mês que você nasceu?')
ano = input ('Qual o ano que você nasceu?')
print('Certo. Você nasceu no dia ',dia,' de ', mes, ' de ',ano, 'Correto?')
print( )
print('------- DESAFIO 03 -------')
pnum = int(input('Qual o primeiro número?'))
snum = int(input('Qual o segundo número?'))
sum = pnum+snum
print('A soma de {} com {} é igual a {}'.format(pnum, snum, sum))
print( )
print('------- DESAFIO 04 -------')
var = input('Digite algo: ')
print('Verificação se o que foi digitado é Alfabético:')
print(var.isalpha())
print('Verificação se o que foi digitado é Numerico:')
print(var.isnumeric())
print('Verificação se o que foi digitado é Alfanumérico:')
print(var.isalnum())
print(type(var))
print( )
print('------- DESAFIO 05 -------')
num = int(input('Digite um número: '))
ant = num-1
sus = num+1
print('Seu sucessor é {}'.format(sus))
print('Seu antecessor é {}'.format(ant))
print( )
print('------- DESAFIO 06 -------')
n = int(input('Digite um número: '))
d = n*2
t = n*3
r = n**(1/2)
print('Seu dobro é {}, seu triplo é {} e sua raiz quadrada é {}'.format(d, t, r))
print( )
print('------- DESAFIO 07 -------')
n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('A média da sua nota é {}'.format(m))
print( )
print('------- DESAFIO 08 -------')
mt = int(input('Digite um valor: '))
cm = mt*100
mm = mt*1000
print('O valor digitado foi {} metros, equivalente a {} centimetros e {} milímetros'.format(mt,cm,mm))
print( )
print('------- DESAFIO 09 -------')
nt = int(input('Digite um número: '))
t0 = nt*0
t1 = nt*1
t2 = nt*2
t3 = nt*3
t4 = nt*4
t5 = nt*5
t6 = nt*6
t7 = nt*7
t8 = nt*8
t9 = nt*9
t10 = nt*10
print('Você digitou o número {} e sua tabuada é'.format(nt))
print('{}*0={}'.format(nt, t0))
print('{}*1={}'.format(nt, t1))
print('{}*2={}'.format(nt, t2))
print('{}*3={}'.format(nt, t3))
print('{}*4={}'.format(nt, t4))
print('{}*5={}'.format(nt, t5))
print('{}*6={}'.format(nt, t6))
print('{}*7={}'.format(nt, t7))
print('{}*8={}'.format(nt, t8))
print('{}*9={}'.format(nt, t9))
print('{}*10={}'.format(nt, t10))
print( )
print('------- DESAFIO 10 -------')
rs = int(input('Digite um valor {acima de 4}: '))
us = rs/3.27
print('Com R${},00 você pode comprar U${}'.format(rs, us))
print( )
print('------- DESAFIO 11 -------')
b = int(input('Digite a largura: '))
h = int(input('Digite a altura: '))
a = b*h
t = a/2
print('Com largura de {} e altura de {} tem-se uma área de {}. São necessários {} litros de tinta  para pintar tudo!'.format(b, h, a, t))
print( )
print('------- DESAFIO 12 -------')
p = float(input('Digite o preço a pagar: '))
desc = p-p*5/100
print('O preço digitado foi de R${} e com 5% de desconto sairá por R${}'.format(p, desc))
print( )
print('------- DESAFIO 13 -------')
sal = float(input('Digite o salário: '))
aum = sal+sal*15/100
print('Seu salário é de R${} e com 15% de aumento será R${}'.format(sal, aum))
print( )
print('------- DESAFIO 14 -------')
t = float(input('Digite a temperatura: '))
tf = ((9* t)/5)+32
print('A temperatura digitada foi de {}ºC ou {}ºF'.format(t, tf))
print( )
print('------- DESAFIO 15 -------')
km = float(input('Quantos km foram percorridos? '))
d = float(input('Por quantos dias? '))
p = 60*d+0.15*km
print('Um carro que rodou {}km por {} dias, terá o valor de R${:.2f} para aluguel.'.format(km, d, p))
print( )
from math import trunc
print('------- DESAFIO 16 -------')
n = float(input('Digite um numero real: '))
nint = trunc(n)
print('O número digitado foi {} e sua parte inteira é {}'.format(n, nint))
print( )
from math import pow
print('------- DESAFIO 17 -------')
co = float(input('Digite o valor do Cateto Oposto: '))
ca = float(input('Digite o valor do Cateto Adjacente: '))
hip = ((pow(co, 2)) + (pow(ca, 2))) **(1/2)
print('Com CO equivalendo {} e o CA a {} O comprimento da hipotenuza é {}'.format(co, ca, hip))
print( )
import math
print('------- DESAFIO 18 -------')
a = float(input('Digite o valor de um angulo qualquer: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('Sobre o Ângulo de {} o seno = {:.2f} O cosseno = {:.2f} e a tangente = {:.2f}'.format(a, s, c, t))
print( )





