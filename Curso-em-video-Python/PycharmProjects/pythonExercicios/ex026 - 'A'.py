frase = input('Digite uma frase: ')
print('''Na frase que você digitou [{}] a letra A aparece {} vezes. 
A primeira vez que ela aparece é na posição vetorial {}. 
A última vez que ela aparece é {}.'''.format(frase, frase.upper().count('A'), frase.upper().find('A'), frase.upper().rfind('A')))
