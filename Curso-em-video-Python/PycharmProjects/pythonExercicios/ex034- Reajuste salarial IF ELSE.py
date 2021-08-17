s = float(input('DIGITE O SEU SALÁRIO: '))
if s > 1250.00:
    print('Seu salário após o aumento de 10% será de: {}'.format(s+s*10/100))
else:
    print('Seu salário após o aumento de 10% será de: {}'.format(s+s*15/100))


