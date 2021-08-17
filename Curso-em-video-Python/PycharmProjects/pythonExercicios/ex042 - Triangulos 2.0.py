r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 and r2 == r3:
        print('Essas três retas formam um triângulo EQUILÁTERO')
    elif r1 != r2  != r3 != r1 :
        print('Essas três retas formam um triângulo ESCALENO')
    else:
        print('Essas três retas formam um triângulo ISÓCELES')
else:
    print('Essas retas não formam um triângulo!')
