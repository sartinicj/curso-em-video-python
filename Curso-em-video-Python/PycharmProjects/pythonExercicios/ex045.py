import random
print('`~´'*10)
op = str(input('''' JOKENPO!
[0] Pedra
[1] Papel
[2] Tesoura
Escolha sua jogada: '''))
pc = ('Pedra', 'Papel', 'Tesoura')
j = random.randint(0, 2)
if op == 0:
    if j == 0:
        print('Você escolheu {}'.format(op))
        print('A máquina escolheu {}'.format(pc[j]))
        print('VOCÊS EMPATARAM! {} com {}}!'.format(op, pc[j]))
elif op == 0:
    if j == 1:
        print('Você escolheu {}'.format(op))
        print('A máquina escolheu {}'.format(pc[j]))
        print('VOCÊS P! {} com {}}!'.format(op, pc[j]))
elif op == 0:
    if j == 2:
        print('Você escolheu {}'.format(op))
        print('A máquina escolheu {}'.format(pc[j]))
        print('VOCÊS G! {} com {}}!'.format(op, pc[j]))
'''
if op == 0 and j == 0:
    print('Você escolheu {}'.format(op))
    print('A máquina escolheu {}'.format(pc[j]))
    print('VOCÊS EMPATARAM! {} com {}}!'.format(op, pc[j]))
elif op == 0 and j == 1:
    print('Você escolheu {}'.format(op))
    print('A máquina escolheu {}'.format(j))
    print('VOCÊS PERDEU! {} com {}}!'.format(op, j))
elif op == 0 and j == 2:
    print('Você escolheu {}'.format(op))
    print('A máquina escolheu {}'.format(j))
    print('VOCÊS GANHOU! {} com {}}!'.format(op, j))
elif op == 1 and j == 1:
    print('Você escolheu {}'.format(op))
    print('A máquina escolheu {}'.format(j))
    print('VOCÊS EMPATARAM! {} com {}}!'.format(op, j))
elif op == 1 and j == 2:
    print('Você escolheu {}'.format(op))
    print('A máquina escolheu {}'.format(j))
    print('VOCÊS PERDEU! {} com {}}!'.format(op, j))
elif op == 1 and j == 0:
    print('Você escolheu {}'.format(op))
    print('A máquina escolheu {}'.format(j))
    print('VOCÊS GANHOU! {} com {}}!'.format(op, j))
elif op == 2 and j == 2:
    print('Você escolheu {}'.format(op))
    print('A máquina escolheu {}'.format(j))
    print('VOCÊS EMPATARAM! {} com {}}!'.format(op, j))
elif op == 2 and j == 0:
    print('Você escolheu {}'.format(op))
    print('A máquina escolheu {}'.format(j))
    print('VOCÊS PERDEU! {} com {}}!'.format(op, j))
elif op == 2 and j == 1:
    print('Você escolheu {}'.format(op))
    print('A máquina escolheu {}'.format(j))
    print('VOCÊS GANHOU! {} com {}}!'.format(op, j))
else:
    print('OPÇÃO INVALIDA!')'''
