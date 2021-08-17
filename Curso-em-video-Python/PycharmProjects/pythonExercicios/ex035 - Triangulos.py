r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Essas três retas formam um triângulo')
else:
    print('Essas retas não formam um triângulo!')
'''
if r1 < (r2-r3)%2 and r1 < r3+r2:
        print('Essas três retas formam um triângulo')
else:
    if r1 > (r3-r2)%2 and r1 < r3+r2:
        print('Essas três retas formam um triângulo')
    else:
        if r2 > (r1 - r3) % 2 and r2 < r1 + r3:
                print('Essas três retas não formam um triângulo')
        else:
            if r2 > (r3-r1)%2 and r1 < r1+r2:
                    print('Essas três retas formam um triângulo')
            else:
                if r3 > (r1 - r2) % 2 and r2 < r1 + r2:
                        print('Essas três retas não formam um triângulo')
                else:
                    if r3 > (r2 - r1) % 2:
                        if r1 < r1 + r3:
                            print('Essas três retas formam um triângulo')
                    else:
                        print('Essas retas não formam um triângulo!')'''









