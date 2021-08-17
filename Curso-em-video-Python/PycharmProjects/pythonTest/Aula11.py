print('''Para colocar cor no Pyhton usa-se o codigo ANSI padrão:
Os estilos usam as numerações principais de 0 a 7. As cores da fonte usam o padrão de 30 a 37 enquanto O background usa de 40 a 47:
\033[0m0 = None\033[m       \033[30m30 = White\033[m      \033[40m40 = White\033[m
\033[1m1 = Bold\033[m       \033[31m31 = Red\033[m        \033[41m41 = Red\033[m
\033[4m4 = Underline\033[m  \033[32m32 = Green\033[m      \033[42m42 = Green\033[m
\033[7m7 = Negative\033[m   \033[33m33 = Yellow\033[m     \033[43m43 = Yellow\033[m
               \033[34m34 = Blue\033[m       \033[44m44 = Blue\033[m
               \033[35m35 = Pink\033[m       \033[45m45 = Pink\033[m
               \033[36m36 = Cian\033[m       \033[46m46 = Cian\033[m
               \033[37m37 = Gray\033[m       \033[47m47 = Gray\033[m

\033[0;33;44m      TESTE    \033[m
\033[7;33;44mTESTE-INVERTIDO\033[m
''')
a= 4
b= 5
print('Os valores são \033[31m{}\033[m e \033[35m{}\033[m!!!'.format(a, b))
print('Uma outra forma de colorir {}{}{} e {}{}{} é colocando o codigo no format!!!'.format('\033[31m', a, '\033[m', '\033[35m', b, '\033[m'))
