import os
os.system('cls')

genero = input('Digite genero: ').upper()

match genero:
    case 'M':
        altura = float(input('Digite sua altura homem: (em metros) '))
        peso = (72.7 * altura) - 58
        print(f'Seu peso ideal é: {peso:.1f} kg')
    case 'F':
        altura = float(input('Digite sua altura mulher: (em metros) '))
        peso = (62.1 * altura) - 44.7
        print(f'Seu peso ideal é: {peso:.1f} Kg')
    case _:
        print('opção invalida')