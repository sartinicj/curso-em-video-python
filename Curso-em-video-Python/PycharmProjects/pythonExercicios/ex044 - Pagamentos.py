p = float(input('Digite o preço: R$'))
op = int(input('''Digite 1 se a forma de pagamento for à vista dinheiro/cheque;
Digite 2 se a forma de pagamento for à vista no cartão;
Digite 3 se a forma de pagamento for em até 2x no cartão;
Digite 4 se a forma de pagamento for em 3x ou mais no cartão;
Escolha a forma da pagamento: '''))
if op == 1:
    desc = p-(p*10/100)
    print('O valor de R${:.2f} á ser pago com 10% de desconto será de R${:.2f}'.format(p, desc))
elif op == 2:
    desc = p-(p*5/100)
    print('O valor de R${:.2f} á ser pago com 5% de desconto será de R${:.2f}'.format(p, desc))
elif op == 3:
    desc = p
    print('O valor de R${:.2f} será pago sem desconto em 2x R${:.2f}'.format(desc, p/2))
elif op == 4:
    parcelas = int(input('Quantas parcelas? '))
    juros = p+(p*20/100)
    div = juros / parcelas
    print('O valor de R${:.2f} á ser pago em {}x de R${:.2f} com 20% de juros terá um total de R${:.2f}'.format(p, parcelas,  div, juros))
else:
    print('OPÇÃO INVALIDA')
