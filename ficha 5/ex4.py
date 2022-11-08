# substitui espaços duplos por espaços únicos

def removeSpaces(texto):
    while texto.find("  ") != -1:
        texto = texto.replace("  "," ")
    print(texto)

texto = input("Insira um texto aqui:")
removeSpaces(texto)