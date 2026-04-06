# Questão 6 - Localizador de Quadrantes (Plano Cartesiano)

print("=== QUADRANTE ===")


x = float(input("X: "))
y = float(input("Y: "))

if x == 0 and y == 0:
    print("Origem")
elif y == 0:
    print("Eixo X")
elif x == 0:
    print("Eixo Y")
elif x > 0 and y > 0:
    print("Quadrante 1")
elif x < 0 and y > 0:
    print("Quadrante 2")
elif x < 0 and y < 0:
    print("Quadrante 3")
else:
    print("Quadrante 4")