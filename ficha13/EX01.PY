from tkinter import *

window = Tk()
window.geometry("1000x500") #(width x height) em px
window.title("ficha 13")
window.resizable(0,0) #colocar 1 se quiser a opcao de redimensionar

screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()

appWidth = 1000 #colocar a width e height do app
appHeight = 500

x = (screenWidth/2) - (appWidth/2)
y = (screenHeight/2) - (appHeight/2)
window.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')

#---------------FUNCOES------------------
def novoJogo():
    print()

def configuracoes():
    print()

#---------------GUI------------------
btnNovoJogo = Button(window, text="Novo jogo", width=15, height=3, command=novoJogo)
btnNovoJogo.place(x=50, y=10)
btnFechar = Button(window, text="Fechar", width=15, height=3, command=window.quit)
btnFechar.place(x=200, y=10)
btnConfig = Button(window, text="Configurações", width=15, height=3, command=configuracoes)
btnConfig.place(x=350, y=10)

window.mainloop()