# Questão 1 - Conta de água

print("=== CÁLCULO DA CONTA DE ÁGUA ===")

consumo_anterior = float(input("Consumo mês anterior: "))
consumo_atual = float(input("Consumo mês atual: "))

# Definir valor por m3
if consumo_atual <= 20:
    valor_m3 = 2.0
elif consumo_atual <= 35:
    valor_m3 = 3.5
elif consumo_atual <= 50:
    valor_m3 = 5.5
else:
    valor_m3 = 7.0

valor = consumo_atual * valor_m3

# Verificar desconto ou multa
if consumo_atual < consumo_anterior:
    desconto = valor * 0.15
    total = valor - desconto
    print("Desconto (15%): R$", desconto)
elif consumo_atual > consumo_anterior:
    multa = valor * 0.10
    total = valor + multa
    print("Multa (10%): R$", multa)
else:
    total = valor

print("Total da conta: R$", total)