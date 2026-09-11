import os
os.system('cls || clear')

print('--- CONVERSOR DE MOEDAS ---')
print('• Dólar')
print('• Euro')
print('• Peso')

# Usamos .lower() para garantir que 'Dolar' vira 'dolar'
opcao = input('\nDigite a moeda para conversão (Dolar, Euro ou Peso): ').lower()
real = float(input('Digite quantos reais você tem: R$ '))

match opcao:
    case 'dolar':
        resultado = real / 5.00  # DIVISÃO em vez de multiplicação
        print(f'\nCom R$ {real:.2f} você compra: $ {resultado:.2f} USD')

    case 'euro':
        resultado = real / 5.50  # DIVISÃO pelo valor do Euro
        print(f'\nCom R$ {real:.2f} você compra: € {resultado:.2f} EUR')

    case 'peso':
        resultado = real / 0.005  # DIVISÃO pelo valor do Peso
        print(f'\nCom R$ {real:.2f} você compra: $ {resultado:.2f} ARS')

    case _:
        print('\nMoeda não reconhecida! Escolha entre Dolar, Euro ou Peso.')