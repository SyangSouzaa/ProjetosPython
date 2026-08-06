def inverte(dicionario: dict) -> dict:
    retorno = {}
    for key in dicionario:
        value = dicionario[key]
        retorno[value] = key
    return retorno

eng_pt = {
    "door": "porta",
    "grape": "uva",
    "apple": "maça",
    "cat": "gato"
}

#criando novas entradas
eng_pt ['orange'] = "laranja"
eng_pt[911] = 190

pt_eng = inverte(eng_pt)

#for value in pt_eng.values():
#    print(value)

for key in pt_eng:
    print(f"{key} => {pt_eng[key]}")
