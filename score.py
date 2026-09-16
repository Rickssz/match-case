import os
os.system('cls || clear')

salario = float(input('Digite seu salário mensal: R$ '))

print('\n--- FAIXA DE SCORE ---')
print('1. Alto  (700 - 1000)')
print('2. Médio (500 - 699)')
print('3. Baixo (0 - 499)')

opcao_score = int(input('\nEscolha a opção do seu score (1, 2 ou 3): '))
emprestimo = float(input('Digite o valor do empréstimo desejado: R$ '))

match opcao_score:
    case 1:
        limite = salario * 15
        if emprestimo <= limite:
            print(f'\nEmpréstimo APROVADO! Valor liberado: R$ {emprestimo:.2f}')
        else:
            print(f'\nEmpréstimo NEGADO! Seu limite máximo é R$ {limite:.2f}')
            
    case 2:
        limite = salario * 8
        if emprestimo <= limite:
            print(f'\nEmpréstimo APROVADO! Valor liberado: R$ {emprestimo:.2f}')
        else:
            print(f'\nEmpréstimo NEGADO! Seu limite máximo é R$ {limite:.2f}')
            
    case 3:
        print('\nEmpréstimo NEGADO! Perfil com Score Baixo não possui limite liberado.')
        
    case _:
        print('\n❌ Opção de menu inválida!')