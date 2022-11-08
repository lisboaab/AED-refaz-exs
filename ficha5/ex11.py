# printCharLine que receba dois argumentos:
#um texto e o nº de caracteres que se pretende imprimir por cada
#linha. A sua função deve imprimir o texto em função desse nº de caracteres, 
#conforme ilustra a imagem abaixo.

def printCharline (texto, caracteres):
    while caracteres < len(texto):
        print(texto[:caracteres])
        texto = texto[caracteres:]
    print(texto)

texto = input("Insira um texto: ")
caracteres = int(input("Quantos caracteres quer por linha? "))
printCharline(texto, caracteres)