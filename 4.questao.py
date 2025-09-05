#atividade 04

import os
os.system("cls")

print("""
\t Fruta \t\t Até 5Kg \t\t Acima de 5Kg
\t Morango \t R$ 2.50 por kg \t R$ 2.20 por kg
\t Maçã \t\t R$ 1.80 pot kg \t R$ 1.50 por kg
""")

morangos = float(input("Digite a quantidade (em Kg) de morangos: "))
macas = float(input("Digite a quantidade (em Kg) de maçãs: "))


if morangos <=5:
    resultado_morango = morangos * 2.50
else:
    resultado_morango = morangos * 2.20


if macas <=5:
    resultado_maca = morangos * 1.80
else:
    resultado_maca = morangos * 1.50

total_morango = morangos * resultado_morango

total_maca = macas * resultado_maca

total = total_maca + total_morango

peso_total = morangos + macas


if peso_total > 10 or total > 15:
    desconto = total * 0.10
    total = desconto
print("=== RESULTADO ===")
print(f"Valor a pagar: R$ {total:.2f}")










