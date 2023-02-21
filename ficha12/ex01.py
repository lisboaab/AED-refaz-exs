from tkinter import *
import os
from datetime import datetime

mainWindow = Tk()
mainWindow.geometry("1000x500") #(width x height) em px
mainWindow.title("Trails App")
mainWindow.resizable(0,0) #colocar 1 se quiser a opcao de redimensionar

screenWidth = mainWindow.winfo_screenwidth()
screenHeight = mainWindow.winfo_screenheight()

appWidth = 1000 #colocar a width e height do app
appHeight = 500

x = (screenWidth/2) - (appWidth/2)
y = (screenHeight/2) - (appHeight/2)
mainWindow.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')

#---------------FUNCOES------------------
def goBack(window):
    """
    Volta pra página anterior"""
    window.destroy()
    mainWindow.deiconify() #restaura a janela anterior

x


def windowMvimentos():
    """
    Nova window do menu "movimentos" """
    mainWindow.withdraw()
    windowMovimentos = Tk()
    windowMovimentos.geometry("800x500")
    windowMovimentos.title("Movimentos")
    windowMovimentos.resizable(0,0)
    windowMovimentos.configure(bg="lightblue")

    screenWidth = windowMovimentos.winfo_screenwidth()
    screenHeight = windowMovimentos.winfo_screenheight()

    appWidth = 1000
    appHeight = 500

    x = (screenWidth/2) - (appWidth/2)
    y = (screenHeight/2) - (appHeight/2)
    windowMovimentos.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
    
    # ---------- MENU --------------
    menu = Menu(windowMovimentos)   #CRIA O MENU
    menu.add_command(label = "Sair", command = windowMovimentos.quit)
    menu.add_command(label="Voltar", command= lambda: goBack(windowMovimentos))
    windowMovimentos.configure(menu = menu, background="lightblue")
    
    
    #-------INTERFACE--------
    global nEstudante
    nEstudante = IntVar()
    lblNumEstudante = Label(windowMovimentos, text="Número estudante:", bg="lightblue")
    lblNumEstudante.place(x=20, y=20)
    entryNumEstudande = Entry(windowMovimentos, width=20, textvariable=nEstudante)
    entryNumEstudande.place(x=150, y=20)

    global selected
    selected = StringVar()
    frameMovimentos= LabelFrame(windowMovimentos, text="Movimentos", width=300, height=100, bg="lightblue")
    frameMovimentos.place(x=20, y=120)
    rdbEntrada = Radiobutton(frameMovimentos, text="Entrada", value="Entrada", variable=selected,  bg="lightblue")
    rdbEntrada.place(x=20, y=20)
    rdbSaida = Radiobutton(frameMovimentos, text="Saida", value="Saida", variable=selected,  bg="lightblue")
    rdbSaida.place(x=20, y=40)

    btnRegistro = Button(windowMovimentos, width=15, height=4, text="Registrar", command=lambda:registro(lboxHistorico))
    btnRegistro.place(x=380, y=140)

    lblHistorico = Label(windowMovimentos, text="Histórico Movimentos")
    lblHistorico.place(x=600, y=20)
    lboxHistorico = Listbox(windowMovimentos, width=40, height=20)
    lboxHistorico.place(x=580, y=50)





#---------------GUI------------------
menuBar = Menu(mainWindow)   #CRIA O MENU

menuBar.add_command(label = "Movimentos", command = windowMvimentos)  # ADICIONA CADA BOTAO/COMANDO AO MENU
menuBar.add_command(label = "Consulta", command = None)
menuBar.add_command(label = "Sair", command = mainWindow.quit)

mainWindow.configure(menu = menuBar, background="lightblue") # ADICIONA O MENU A PÁGINA(WINDOW)

imgPrincipal = PhotoImage(file = ".//ficha12//images//img-gestao.png")
labelImgPrincipal = Label(mainWindow, image=imgPrincipal, width = 600)
labelImgPrincipal.place(x=0, y=0)

titulo = Label(mainWindow, text="Gestor de presenças", bg="lightblue", font=14)
titulo.place(x=700, y= 230)
mainWindow.mainloop()