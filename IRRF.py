import os
os.system('cls')

salario_bruto = float(input('digite o seu salario: '))

print('\nREGIME DE TRABALHO: CLT | PJ')
regime = input('Digite o tipo de regime que você faz: ').upper()

match regime:
    case 'PJ':
        imposto = 0.0
        aliquota = '0%'
        print("Regime PJ: Imposto retido R$ 0.00")
    case 'CLT' if salario_bruto <= 2259.20:
        imposto = 0.0
        aliquota = '0%'
        print("Regime CLT com salario de 2.259.20: Imposto retido R$ 0.00")
    case 'CLT' if salario_bruto <= 5000.00:
        imposto = salario_bruto * 0.15
        aliquota = '15%'
    case 'CLT' if salario_bruto > 5000.00:
        imposto = salario_bruto * 0.275
        aliquota = '27.5%'
    case _:
        imposto = None

if imposto is not None:
    salario_liquido = salario_bruto - imposto
    print('\n--- RESUMO DO IRRF ---')
    print(f'Regime: {regime}')
    print(f'Salário Bruto: R$ {salario_bruto:.2f}')
    print(f'Alíquota: {aliquota}')
    print(f'Imposto Retido: R$ {imposto:.2f}')
    print(f'Salário Líquido: R$ {salario_liquido:.2f}')
else:
    print('\n Opção de regime inválida! Operação cancelada.')
