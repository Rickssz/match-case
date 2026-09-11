import os
os.system('cls')

A = int(input('digite o valor de A: '))
B = int(input('digite o valor de B: '))
C = int(input('digite o valor de C: '))

if (A + B) > C:
    print(f'A + B é igual: {A + B} q é maior q {C}')
else:
    print(f'A + B é igual: {A + B} q é menor q C: {C}')