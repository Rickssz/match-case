import os
os.system('cls || clear')

valor_total = float(input('Digite o valor total da compra: R$ '))

print('\nTIPOS DE CLIENTE: VIP | COMUM')
cliente = input('Digite o tipo de cliente que você é: ').upper()

match cliente:
    case 'VIP' if valor_total > 500.00:
        desconto = 0.20
        msg = 'Parabéns! Você é VIP e comprou acima de R$ 500.00 (20% OFF).'

    case 'VIP':
        desconto = 0.10
        msg = 'Parabéns! Você é VIP e comprou até R$ 500.00 (10% OFF).'

    case 'COMUM' if valor_total > 500.00:
        desconto = 0.05
        msg = 'Você é cliente COMUM e comprou acima de R$ 500.00 (5% OFF).'

    case 'COMUM':
        desconto = 0.00
        msg = 'Você é cliente COMUM e comprou até R$ 500.00 (Sem desconto).'

    case _:
        desconto = 0.00
        msg = 'Tipo de cliente inválido!'

# Exibição unificada:
valor_desconto = valor_total * desconto
valor_final = valor_total - valor_desconto

print('\n--- RESUMO DA COMPRA ---')
print(msg)
print(f'Valor original: R$ {valor_total:.2f}')
print(f'Desconto: R$ {valor_desconto:.2f}')
print(f'Valor final: R$ {valor_final:.2f}')