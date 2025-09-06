#atividade 10

import os
os.system("cls")

combustivel = input ("Qual o tipo de combustível ( A OU G ): ")

preco_g = 6.59
preco_a = 3.79
valor_desconto = 10 / 100
valor_desconto_2 = 20 / 100
valor_desconto_3 = 15 / 100
valor_desconto_4 = 30 / 100

match combustivel:
    case "g":
        litros = float(input("Digite a quantidade em litros do combustível: "))
        if litros <= 25:
            resultado_gasolina_1 = litros * preco_g 
            valor_desconto = resultado_gasolina_1 * valor_desconto_3 
            valor_total_gasolina = resultado_gasolina_1 - valor_desconto 
            print(f"total a pagar de gasolina é: {valor_total_gasolina:.2f}")
        else:
            resultado_gasolina_2 = litros * preco_g 
            valor_desconto = resultado_gasolina_2 * valor_desconto_4 
            valor_total_gasolina = resultado_gasolina_2 - valor_desconto 
            print(f"total a pagar de gasolina é: {valor_total_gasolina:.2f}")
    case "a":
        litros = float(input("Digite a quantidade em litros do combustível: "))
        if litros <= 25:
            resultado_alcool_1 = litros * preco_a
            valor_desconto_a =resultado_alcool_1 * valor_desconto
            valor_total_alcool = resultado_alcool_1 - valor_desconto_a 
            print(f"O valor do seu álcool: {valor_total_alcool:.2f}")
        else: 
            resultado_alcool_2 = litros * preco_a
            valor_desconto_a = resultado_alcool_2 * valor_desconto_2
            valor_total_alcool_2 = resultado_alcool_2 - valor_desconto_a 
            print(f"O valor do seu álcool: {valor_total_alcool_2:.2f}")
    case _:
        print("letra invalida para identificar o combustível!!")

            

