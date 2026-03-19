#print("Hoje esta quente, mas choveu")
#print("Se chover, São Paulo fica com trânsito")
#print("E os semáforos normalmente acabam com problemas")
#print("O metrô também fica com velocidade reduzida.")

salario = float(input("Salário: "))

if salario <= 1621:
    inss = salario * 7.5 / 100

if salario > 1621 and salario <= 2902.84:
    inss = 1621 * 0.075 # (7,5%)
    inss = inss + (salario - 1621) * 0.9

if salario > 2902.84 and salario <= 4354.27:
    inss = 1621 * 0.075
    inss = inss + (2902.84 - 1621)* 0.09
    inss = inss + (salario - 4354.27) * 0.12

if salario > 4354.27 and salario <= 8475.55:
    inss = 1621 * 0.075
    inss = inss + (2902.84 - 1621)* 0.09
    inss = inss + (salario - 4354.27) * 0.12
    inss = inss + (salario - 8475.55 ) * 0.14

if salario > 4354.27 and salario <= 8475.55:
    inss = 1621 * 0.075
    inss = inss + (2902.84 - 1621) * 0.09
    inss = inss + (salario - 4354.27) * 0.12
    inss = inss + (salario - 8475.55) * 0.14
    inss = inss + (8475.55 - 4352.27) * 0.14

    
print(f"Desconto INSS é {inss}")