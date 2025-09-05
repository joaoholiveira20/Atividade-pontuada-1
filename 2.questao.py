# atividade 02

import os
os.system("cls")

#Pedindo Dados
nome = input("Digite seu nome: ")
sexo = input("Digite seu gênero ( F OU M ): ")
civil = input("Digite o seu estado civil: ")

#caso seja casada e o gênero seja "f"
match sexo:
    case "f":
        if civil == "casada":
            tempo_casada = int(input("Digite o tempo de casada em anos: ")) 
            print("=== RESULTADO ===")
            print(f"Seu nome: {nome}")
            print(f"Seu gênero: {sexo}")
            print(f"Seu estado civil: {civil}")
            print(f"Seu tempo de casada: {tempo_casada} Anos ")
        else:
            print("=== RESULTADO ===") #caso seja as outras opções e o gênero sendo "f"
            print(f"Seu nome: {nome}")
            print(f"Seu gênero: {sexo}")
            print(f"Seu estado civil: {civil}")
    case _:
        print("=== RESULTADO ===") #caso seja " m "
        print(f"Seu nome: {nome}")
        print(f"Seu gênero: {sexo}")
        print(f"Seu estado civil: {civil}")
        
       







