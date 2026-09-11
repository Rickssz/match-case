import os
os.system('cls')

dia = int(input('Digite o dia da semana: '))

match dia:
    case 1:
        print('Domingo é final de semana')
    case 2:
        print('Segunda-feira, não é final de semana')
    case 3:
        print('Terça-feira, não é final de semana')
    case 4:
        print('Quarta-feira, não é final de semana')
    case 5:
        print('Quinta-feira, não é final de semana')
    case 6:
        print('Sexta-feira, não é final de semana')
    case 7:
        print('Sabado, é final de semana')
    case _:
        print('Numero invalido')