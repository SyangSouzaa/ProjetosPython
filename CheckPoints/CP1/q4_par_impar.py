# Questão 4 - Impar e Par

print("=== VERIFIQUE QUANTIDADE DE IMPAR E PAR ===")

quantidade = int(input("Quantos números: "))

pares = 0
impares = 0

for i in range(quantidade):
    num = int(input("Digite um número: "))

    if num % 2 == 0:
        print("PAR")
        pares += 1
    else:
        print("ÍMPAR")
        impares += 1

print("Total de pares:", pares)
print("Total de ímpares:", impares)