num = int(input('Digite um número: '))
op = int(input('''Escolha:
1 - Conversão binária;
2 - Conversão octal;
3 - conversão hexadecimal;
'''))
if op == 1:
    binary = format(num, 'b')
    print('Após escolher a opção {}, opnúmero {} em sua forma Binária equivale à {}'.format(op, num, binary))
elif op == 2:
    octal = format(num, 'o')
    print('Após escolher a opção {}, o número {} em sua forma Octal equivale à {}'.format(op, num, octal))
else:
    hexa = format(num, 'x')
    print('Após escolher a opção {}, o número {} em sua forma Hexadecimal equivale à {}'.format(op, num, hexa))
