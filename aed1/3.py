#  leia um texto e o nº de caracteres que se pretende imprimir por cada linha.

def caracLinha(texto, caractere):
    """ le um texto e o numero de caracteres pra imprimir em cada linha """
    if 1<= caractere <= 12:
        while len(texto) >= caractere:
            print(texto[:caractere])
            texto = texto[caractere:]
        print(texto)
    else:
        print("Insira um número entre 1 e 12!")

texto = input("Insira um texto: ")
caractere = int(input("Quantos caracteres por linha? (1-12) "))
caracLinha(texto, caractere)