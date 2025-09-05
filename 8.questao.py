#atividade 08

import os
os.system("cls")

cor = input ("informe a cor do CD sendo verde, azul, amarelo, vermelho: ")

match cor:
    case "verde":
        print("Preço: R$ 10,00")
    case "azul":
        print("Preço: R$ 20,00")
    case "amarelo":
        print("Preço: R$ 30,00")
    case "vermelho":
        print("Preço: 40,00")
    case _:
        print("Não temos essa cor..")
