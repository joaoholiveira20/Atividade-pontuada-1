#Atividade 03

import os
os.system("cls")

n1 = int(input("Digite o valor A: "))
n2 = int(input("Digite o valor B: "))

if n1 == n2:
    resultado = n1 + n2
    print("=== RESULTADO ===")
    print(f"""
    Valor A: {n1}
    Valor B: {n2}
    """)
    print(f"os valores de A e B são iguais ent eles vão se somar")
    print(f"Valor C: {resultado}")
else:
    resultado = n1 * n2
    print("=== RESULTADO ===")
    print(f"""
    Valor A: {n1}
    Valor B: {n2}
    """)
    print("são diferentes então iram se multiplicar")
    print(f"Valor C: {resultado}")    
