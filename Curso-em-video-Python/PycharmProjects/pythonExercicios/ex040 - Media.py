n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
if m < 5.0:
    print('REPROVADO. Sua média é {}'.format(m))
elif m >= 7.0:
    print('APROVADO. Sua média é {}'.format(m))
else:
    print('RECUPERAÇÃO. Sua média é {}'.format(m))