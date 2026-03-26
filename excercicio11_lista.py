valor = float(input("Valor da compra: "))
print("1 - dinheiro ou cheque, 10% de desconto")
print("2 - cartão de crédito, 5% de desconto")
print("3 - 2x preco normal")
print("4 - 4x acréscimo de 7%")

forma_pgto = int(input("escolha uma das opcoes acima: "))

match forma_pgto:
  case 1:
    desc = valor * 0.1
    print(f"O desconto foi de {desc}, você pagará {valor - desc}")
  case 2:
      desc = valor * 0.5
      print(f"O desconto foi de {desc}, você pagará {valor - desc}")
  case 3:
      parcela = valor / 2
      print(f"Você pagará 2 x {parcela}")
  case 4:
      acrescimo = valor * 0.07
      parcela = (valor + acrescimo) / 4
      print(f"O valor do produto será de {valor + acrescimo} em 4x {parcela}")
  case _:
      print("Forma de pagamento inválida")
