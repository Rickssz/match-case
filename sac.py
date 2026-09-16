import os
os.system('cls')

# mostrando as opções:
print('---OPÇÕES---')
print('1. Financeiro')
print('2. Suporte Técnico')
print('3. Cancelamento')
print('4. Sair\n')

# pedindo a opção escolhida:
opcao = int(input('Escolha um das opções anteriores (1, 2, 3 ou 4): '))

# processamento e saida: 
match opcao:
    case 1:
        fatura = float(input('\nDigite o valor da fatura atrasada: '))
        if fatura > 100.00:
            fatura_com_multa = fatura * 1.10
            print(f'Valor com multa de 10%: R$ {fatura_com_multa:.2f}')
        else:
            print(f'Valor a pagar (Sem multas): R$ {fatura:.2f}')            
    case 2:
        problema = input('\nDigite o problema enfrentado: ').upper()
        if problema == 'INTERNET':
            print('Orientação: Reinicie o modem da tomada e aguarde 2 minutos.')
        elif problema == 'ROTEADOR':
            print("Orientação: Verifique se os cabos estão firmemente conectados.")
        else:
            print("Problema não identificado. Transferindo  para um atendente...")            
    case 3:
        print("\nLamentamos a sua saída. Sua solicitação foi enviada para o setor de retenção.")
    case 4:
        print("Atendimento finalizado. Obrigado!")
    case _:
        print('\nOpção inválida! Escolha um número de 1 a 4.')
input('\nPressione ENTER para continuar...')