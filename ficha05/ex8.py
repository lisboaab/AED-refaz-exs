def replaceNumbers(texto):
    texto = texto.replace ("1","um")
    texto = texto.replace("2", "dois") 
    texto = texto.replace("3", "três")
    texto = texto.replace("4", "quatro")
    texto = texto.replace("5", "cinco")
    texto = texto.replace("6", "seis")
    texto = texto.replace("7", "sete")
    texto = texto.replace("8", "oito")
    texto = texto.replace("9", "nove")
    texto = texto.replace("0", "zero")
    print(texto)


texto = input("Insira um texto: ")
replaceNumbers(texto)
