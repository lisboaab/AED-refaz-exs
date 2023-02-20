import os

def lerFicheiro():
    """
    return text file, codified by cifra cesar
    """
    fileTexto = open(file, "r", encoding="utf-8")
    textoCodificado = fileTexto.read()
    fileTexto.close() 
    return textoCodificado


def decript(textoCodificado):
    """
    Decodes string text
    """
    texto= ""
    for char in textoCodificado:
        posicaoASCII = ord(char)
        novocaracter = chr(posicaoASCII - chave)
        texto+= novocaracter
    return texto


def encript(texto, chave):
    """
    it receives a string and a key (Cifra Cesar)
    """
    textoCodificado= ""
    for char in texto:
        posicaoASCII = ord(char)
        novocaracter = chr(posicaoASCII+ chave)
        textoCodificado+= novocaracter
    return textoCodificado


def guardaFicheiro(textoCodificado):
    fileTexto = open(file, "w", encoding="utf-8")
    fileTexto.write(textoCodificado)
    fileTexto.close()
    print("Texto guardado em ficheiro...")
    input()





file = ".\\ficha10\\ficheiros\\test.txt"
pasta = "ficheiros"
chave = 5

if not os.path.exists(pasta):
    os.mkdir(pasta)

resp = "1"

while resp != "0":
    print("\t MENU \n 1 - Escreve ficheiro \n 2 - Ler ficheiro \n 0 - Sair")
    resp = input("Esolha uma opção: ")
    if resp == "1":
        texto = input("Texto: ")
        textoCodificado= encript(texto, chave)  
        guardaFicheiro(textoCodificado)
    elif resp == "2":
        textoCodificado = lerFicheiro()
        print("Texto descodificado:", decript(textoCodificado))
        input()
    else:
        resp = "0"