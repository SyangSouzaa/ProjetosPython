salario = float(input("Salario: "))
if salario <= 1621:
    inss = salario * 7.5 / 100
else:
    inss = 1621 * 0.075
    if salario <= 2902.84:
        inss = inss + (salario - 1621) * 0.09
    else:
        inss = inss + (2902.84 - 1621) * 0.09
        if salario <= 4354.27:
            inss = inss + (salario - 2902.84) * 0.12
        else:
            inss = inss + (4354.27 - 2902.84) * 0.12
            if salario <= 8475.55:
                inss = inss + (salario - 4354.27) * 0.14
            else:
                inss = inss + (8475.55 - 4354.27) *0.14

print(f"Desconto INSS é {inss}")