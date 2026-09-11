import os
os.system('cls')

nome = input("digite seu nome: ")
sexo = input("digite seu sexo : ")
civil = input("digite seu estado civil: ")

if sexo == 'feminino' and civil == 'casada':
    casada = int(input('digite o tempo de casada: '))

    print(f'\n---RESUMO---')
    print(f'\nSeu nome é: {nome}')
    print(f'Seu sexo é: {sexo}')
    print(f'Seu estado civil é: {civil}')
    print(f'Seu tempo casada é: {casada} anos')
else:
    print('Invalido')