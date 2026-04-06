# Questão 5 - Urna Eletrônica Simplificada

print("=== URNA ===")

a = b = nulo = branco = 0

while True:
    voto = int(input("Digite seu voto: "))

    if voto == 0:
        break
    elif voto == 1:
        a += 1
    elif voto == 2:
        b += 1
    elif voto == 3:
        nulo += 1
    elif voto == 4:
        branco += 1
    else:
        print("Voto inválido")

print("Candidato A:", a)
print("Candidato B:", b)
print("Nulos:", nulo)
print("Brancos:", branco)