import os
os.system('cls')

A = int(input('digite o valor de A: '))
B = int(input('digite o valor de B: '))
C = (A, B)

if A == B:
    C = A + B
else:
    C = A * B

print(f'O resultado final é {C}')

