from tkinter import *
import os

# ------- GUI -----------

window = Tk()
window.geometry("800x500")
window.title("Ex 01")

screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()

appWidth = 800 #colocar a width e height do app
appHeight = 500

x = (screenWidth/2) - (appWidth/2)
y = (screenHeight/2) - (appHeight/2)
window.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')

# ------- FUNCOES -----------
pasta = "ex01"
ficheiro = ".\\ficha11\\ex01\\texto.txt"
global wgtText

def guardar():
    """
    Guarda o texto do widget "texto" dentro do arquivo txt"""
    
    global wgtText
    if not os.path.exists(pasta):  #cria a pasta se ela nao existir
        os.mkdir(pasta)
    
    ntexto = wgtText.get("0.0","end-1c")    # end - 1 caracter (\n)
    file = open(ficheiro, "w", encoding="utf-8")  #se o ficheiro já existir apaga o conteudo dele
    file.write(ntexto)
    

def limpar():
    """
    Limpa o widget texto"""
    
    global wgtText
    wgtText.delete("0.0", "end")

def ler():
    """
    Le o que está no ficheiro e coloca no widget texto"""
    
    global wgtText
    file = open(ficheiro, "r", encoding="utf-8")  #se o ficheiro já existir apaga o conteudo dele
    textoFicheiro= file.readlines()
    file.close()

    for linha in textoFicheiro:
        wgtText.insert("end", linha)

        
#--------- BOTOES -----------
btnGuardarFile = Button(window, text="Guardar ficheiro", command=guardar)
btnGuardarFile.place(x=20, y=50)

btnLimpar = Button(window, text="Limpar", command=limpar)
btnLimpar.place(x=20, y=150)

btnLerFile = Button(window, text="Ler ficheiro", command=ler)
btnLerFile.place(x=20, y=250)

wgtText = Text(window, wrap="word", width=70)
wgtText.place(x= 200, y=20)


window.mainloop()