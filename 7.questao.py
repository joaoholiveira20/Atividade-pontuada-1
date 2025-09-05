#atividade 07

import os
os.system("cls")

nome = input("Dgite o nome do produto: ")
quantidade = int(input("Digite a quantidade adquirida: "))
preco = int(input("preço unitário do produto: "))

total = quantidade * preco

if quantidade <= 5:
    desconto = quantidade * 0.02
elif quantidade >5 and quantidade <= 10:
    desconto = quantidade * 0.03
else:
    desconto = quantidade * 0.05