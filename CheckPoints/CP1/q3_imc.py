# Questão 3 - IMC

print("=== CALCULE SEU IMC ===")

peso = float(input("Peso: "))
altura = float(input("Altura: "))

imc = peso / (altura ** 2)

print("IMC:", imc)

if imc < 18.5:
    print("Abaixo do peso")
elif imc <= 24.9:
    print("Peso normal")
elif imc <= 29.9:
    print("Sobrepeso")
else:
    print("Obesidade")