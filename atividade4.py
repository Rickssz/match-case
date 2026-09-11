import os
os.system('cls')

maca = 1.80
morango = 2.50

print('Frutas disponíveis:')
print('1. Morango por R$ 2,50/kg')
print('2. Maçã por R$ 1,80/kg')
print('Caso compre mais de 10kg ou o total ultrapasse R$ 15,00, ganhe 10% de desconto!\n')

opcao = input('Digite a fruta que quer (maca / morango): ').strip().lower()

match opcao:
    case 'maca' | 'maça' | 'maçã' | '2':
        quilos = float(input('Digite quantos Kg quer: '))
        valor = maca * quilos

        if quilos >= 10 or valor >= 15:
            desconto = valor * 0.10
            valor_final = valor - desconto
            print('Desconto de 10% aplicado!')
        else:
            valor_final = valor

        print(f'Total a pagar: R$ {valor_final:.2f}')

    case 'morango' | '1':
        quilos = float(input('Digite quantos Kg quer: '))
        valor = morango * quilos

        if quilos >= 10 or valor >= 15:
            desconto = valor * 0.10
            valor_final = valor - desconto
            print('Desconto de 10% aplicado!')
        else:
            valor_final = valor

        print(f'Total a pagar: R$ {valor_final:.2f}')

    case _:
        print('Opção inválida!')