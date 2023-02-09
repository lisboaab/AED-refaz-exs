import os

def escreveTexto(texto):
    file = open("file", "wb")
    texto1 = bytes(texto, encoding="utf-8")
    file.write(texto1)
    file.close()
    
def lerTexto():
    file = open("file", "rb")
    texto = str(file.read())
    file.close()
    print(texto)

file = ".\\ficha10\\ficheiros\\dados.bin"
pasta = "ficheiros"
if not os.path.exists(pasta):
    os.mkdir(pasta)

texto = input("Insira um texto: ")
escreveTexto(texto)
lerTexto()