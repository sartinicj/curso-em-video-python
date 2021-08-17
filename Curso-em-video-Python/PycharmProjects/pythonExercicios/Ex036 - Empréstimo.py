valcasa = float(input('Digite o valor da casa: '))
sal = float(input('Digite o valor do seu salário: '))
pag = float(input('Em quantos anos quer pagar? '))
prest = valcasa/(pag*12)
if prest <= sal*30/100:
    print('EMPRESTIMO APROVADO! O valor da prestação mnesal será de R${} '.format(prest))
else:
    print('EMPESTIMO NEGADO.')
