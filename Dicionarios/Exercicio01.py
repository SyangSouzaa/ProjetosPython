texto = input("Digite uma frase: ").lower()

contagem = {}

for letra in texto:
    if letra.isalpha():  # Conta apenas letras
        if letra in contagem:
            contagem[letra] += 1
        else:
            contagem[letra] = 1

for letra in sorted(contagem):
    print(letra, ":", contagem[letra])