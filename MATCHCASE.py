import os
os.system('cls')

n1 = int(input('digite o n1: '))
n2 = int(input('digite o n2: '))
caracter = input('digite o caracter: ')

match caracter:
    case "+":
        print(n1 + n2)
    case "-":
        print(n1 - n2)
    case "/":
        print(n1 / n2)
    case "*":
        print(n1 * n2)