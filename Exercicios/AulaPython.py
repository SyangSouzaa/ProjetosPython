
"""#Recebe Nome e Sobrenome(1)
nome = input("Nome: ")
ano = int(input("Ano de nascimento: "))
idade = 2026 - ano

print("Nome:", nome, "Idade: ", idade)"""


"""#Potencia(5)
num1 = int(input("Digite um número: ")) 
num2 = int(input("Digite outro número: "))

potencia = num1 ** num2

print(f"A potencia é: {potencia}")"""

#Calculando Porcentagem(9)
preco = float(input("Digite o preço do produto: "))
aumentopercentual = float(input("Digite o aumento em %: "))

aumento = preco * aumentopercentual / 100
preco_final = preco + aumento

print(preco_final)
