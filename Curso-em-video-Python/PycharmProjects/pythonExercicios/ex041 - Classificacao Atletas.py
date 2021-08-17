from datetime import date
nasc = int(input('Digite o ano do seu nascimento: '))
cat = date.today().year - nasc
if cat <=9:
    print('Você se enquadra na categoria MIRIM ')
elif cat <= 14:
    print('Você se enquadra na categoria INFANTIL ')
elif cat <= 19:
    print('Você se enquadra na categoria JUNIOR ')
elif cat <= 25:
    print('Você se enquadra na categoria SÊNIOR ')
else:
    print('Você se enquadra na categoria MASTER ')