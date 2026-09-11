import os
os.system('cls')

print("=== CARDÁPIO DO RESTAURANTE ===")
print("1. PICANHA          || R$ 25,00")
print("2. LASANHA          || R$ 20,00")
print("3. STROGONOFF       || R$ 18,00")
print("4. BIFE ACEBOLADO   || R$ 15,00")
print("5. PÃO COM OVO      || R$  5,00")

codigo = int(input("\nDigite o código da comida que você quer: "))

match codigo:
    case 1:
        print("\n-> Seu pedido: 1x PICANHA")
        print("-> Valor total: R$ 25,00")
    case 2:
        print("\n-> Seu pedido: 1x LASANHA")
        print("-> Valor total: R$ 20,00")
    case 3:
        print("\n-> Seu pedido: 1x STROGONOFF")
        print("-> Valor total: R$ 18,00")
    case 4:
        print("\n-> Seu pedido: 1x BIFE ACEBOLADO")
        print("-> Valor total: R$ 15,00")
    case 5:
        print("\n-> Seu pedido: 1x PÃO COM OVO")
        print("-> Valor total: R$ 5,00")
    case _:
        print("\nCódigo inválido! Digite um número de 1 a 5.")