v = int(input('Qual a velocidade que você estava?'))
if v > 80:
    multa = 7*(v-80)
    print ('Você recebeu uma multa de R${},00'.format(multa))
else:
    print('Você não foi multado')