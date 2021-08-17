f = m = 1
s = str(input('Digite a letra do sexo: '))
while s == 0:
    if s == 'F' or s == 'f' and s == 'M' or s == 'm':
        print('Parabéns você digitou o esperado!')
    else:
        print('O digitado não é o esperado. Tente de novo, ou 0 para encerrar.')
print('Fim de execução.')

#NÃO ESTÁ LENDO IF E ELSE