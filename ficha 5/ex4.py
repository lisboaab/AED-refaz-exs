# substitui espaços duplos por espaços únicos

def removeSpaces(texto)
    espacoSingle = " "
    espacoDuplo = texto.find("  ")
    if espacoDuplo != -1:
        espacoDuplo = espacoSingle
    print(texto)

texto = input("Insira um texto aqui:")
removeSpaces(texto)