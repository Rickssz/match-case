import os
os.system('cls || clear')

valor = float(input('Digite o valor do produto: R$ '))

print('\n1. Pagamento à vista (10% de desconto)')
print('2. Pagamento parcelado')

opcao = int(input('\nDigite a opção desejada: '))

match opcao:
    case 1:
        desconto = valor * 0.10
        total = valor - desconto
        
        print(f'\n--- RESUMO DO PAGAMENTO ---')
        print(f'Valor do produto: R$ {valor:.2f}') 
        print('Forma de pagamento: À vista')
        print(f'Valor do desconto: R$ {desconto:.2f}') 
        print(f'Valor total a pagar: R$ {total:.2f}')
        
    case 2:
        parcela = int(input('Digite a quantidade de parcelas: '))
        valor_parcela = valor / parcela
        
        print(f'\n--- RESUMO DO PAGAMENTO ---')
        print(f'Valor do produto: R$ {valor:.2f}') 
        print('Forma de pagamento: Parcelado')
        print(f'Quantidade de parcelas: {parcela}x') 
        print(f'Valor de cada parcela: R$ {valor_parcela:.2f}')
        print(f'Valor total a pagar: R$ {valor:.2f}')
        
    case _:
        print('\nOpção inválida! Escolha 1 para à vista ou 2 para parcelado.')