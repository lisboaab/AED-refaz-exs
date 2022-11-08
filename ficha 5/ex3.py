# capicua

def capicua(texto):
    capicua = ""
    tam = len(texto)
    for i in range(tam-1, -1, -1):
        capicua += texto[i]
    if texto == capicua:
        return True
    else: 
        return False

texto = input("Insura uma palavra: ")
if capicua(texto):
    print("É uma capicua!")
else:
    print("Não é uma capicua.")
