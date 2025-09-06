#atividade 09

import os
os.system("cls")

renda = float(input("Digite a sua renda mensal: "))
emprestimo = float(input("Valor total do empréstimo: "))
parcela = int(input("Digite o número de prestações: "))

calculo_mensal = renda * 10
limite_prestacao = renda * 0.3
prestacao = emprestimo / parcela


if emprestimo > calculo_mensal:
    resultado = "O seu valor de emprestimo deve ser menor do que 10 vezes o valor da sua renda!! "
elif prestacao <= limite_prestacao and prestacao <= calculo_mensal:
    resultado = "Aprovado!!"
else:
    resultado = "Negado!!"



print(f"o resultado do seu empréstimo: {resultado}")