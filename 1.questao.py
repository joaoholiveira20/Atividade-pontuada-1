#atividade 01

import os
os.system("cls")

n1 = int(input("Digite o valor A: "))
n2 = int(input("Digite o valor B: "))
n3 = int(input("Digite o valor C: "))

if n1 + n2 <n3:
    resultado = n1 + n2 
    print("=== RESULTADO ===")
    print(f"Valor de C: {n3}")
    print(f"Resultado da soma: {resultado}")
    print("A soma dos valores A e B é menor do que o valor C ")
else:
    resultado = n1 + n2
    print("=== RESULTADO ===")
    print(f"Valor de C: {n3}")
    print(f"Resultado da soma: {resultado}")
    print("A soma dos valores A e B é maior do que o valor C ")
