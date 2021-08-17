v = float(input('Qual a distância da viagem? '))
preco = v*0.5 if v <=200 else v*0.45
print('O valor será de R${}'.format(preco))