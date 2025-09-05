#atividade 06


import os
os.system ("cls")


n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media = (n1 + n2) / 2

if media >=6:
    resultado = "PARABÉNS!! FOI APROVADO!!"
elif media >=4.1 or media >=5.9:
    resultado = "Está na recuperação!!"
else:
    resultado = "Voçe estar reprovado!!"

print(f"sua média: {media}")
print(f"Seu  resultado: {resultado}")