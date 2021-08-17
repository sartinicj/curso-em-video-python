print('------- DESAFIO 15 -------')
km = float(input('Quantos km foram percorridos? '))
d = float(input('Por quantos dias? '))
p = 60*d+0.15*km
print('Um carro que rodou {}km por {} dias, terá o valor de R${:.2f} para aluguel.'.format(km, d, p))
