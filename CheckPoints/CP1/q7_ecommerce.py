# Questão 7 - Calculadora de Descontos e Frete

print("=== E-COMMERCE ===")

valor = float(input("Valor da compra: "))
tipo = int(input("Tipo (1-Comum, 2-VIP, 3-Premium): "))

desconto = 0

if tipo == 2 and valor > 100:
    desconto = valor * 0.05
elif tipo == 3:
    if valor > 500:
        desconto = valor * 0.15
    else:
        desconto = valor * 0.10

valor_final = valor - desconto

# Frete
if valor_final < 200:
    frete = 25
else:
    frete = 0

total = valor_final + frete

print("Desconto: R$", desconto)
print("Frete: R$", frete)
print("Total: R$", total)