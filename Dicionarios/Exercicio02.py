eng_pt = {
    "door": "porta",
    "grape": "uva",
    "apple": "maça",
    "cat": "gato"
}

#criando novas entradas
eng_pt ['orange'] = "laranja"
eng_pt[911] = 190

for key in eng_pt:
    print(key)

for value in eng_pt.values():
    print(value)