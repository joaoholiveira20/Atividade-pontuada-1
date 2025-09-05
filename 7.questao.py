#atividade 07

import os
os.system("cls")

nome = input("Dgite o nome do produto: ")
quantidade = int(input("Digite a quantidade adquirida: "))
preco = float(input("preço unitário do produto: "))

total = quantidade * preco

if quantidade <= 5:
    desconto = quantidade + preco * 0.02
    total_desconto = desconto
elif quantidade >5 and quantidade <= 10:
    desconto = quantidade + preco * 0.03
    total_desconto = desconto - preco
else:
    desconto = quantidade + preco * 0.05
    total_desconto = desconto - preco

total = quantidade * preco
total_com_desconto = total - total_desconto

print(f"total da compra: {total}")
print(f"o desconto: {desconto}")
print(f"total a pagar: {total_com_desconto}")
