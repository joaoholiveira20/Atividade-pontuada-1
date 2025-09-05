#Atividade 5

import os 
os.system("cls")

n1 = int(input("Dgite o número A: "))
n2 = int(input("Digite o número B: "))
carac = input ("Digite um caracter: ")

match carac:
    case "+":
        resultado = n1 + n2
    case "*":
        resultado = n1 * n2
    case "-":
        resultado = n1 - n2
    case "/":
        resultado = n1 / n2
    case _:
        resultado = "opção inválida"

print(f"número A: {n1}")
print(f"número B: {n2}")
print(f"operador escolhido: {carac}")
print(f"Resultado: {resultado}")
