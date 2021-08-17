a = int(input('Digite o ano para saber se é bissexto: '))
print('É bissexto' if a%4 == 0 and a%100 != 0 or a%400 == 0 else 'Não é bissexto')

from datetime import date
a = int(input('Digite o ano para saber se é bissexto, ou 0 para analisar o ano atual: '))
if a == 0:
    a = date.today().year
    print('É bissexto' if a % 4 == 0 and a % 100 != 0 or a % 400 == 0 else 'Não é bissexto')

'''if a%4 == 0 and a%100 != 0 or a%400:
    print('É bissexto')
else:
    print('Nãao é bissexto')'''