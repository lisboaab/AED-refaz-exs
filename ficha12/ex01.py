from tkinter import *
import os
from datetime import datetime

# ---------- FUNCOES --------------


def registro(num,selected):
    ficheiro = ".\\ficha12\\files\\acessos.txt"
    pasta = ".\\ficha12\\files"

    if not os.path.exists(pasta):    #cria a pasta se ela não existir
        os.mkdir(pasta)
        
    dataEhora= datetime.now()
    data= dataEhora.strftime("%d/%m/%Y")
    hora =dataEhora.strftime("%H:%M")

    
    f = open(ficheiro, "a", encoding="utf-8")
    linha = str(num.get()) + ";" + data + ";" + hora + ";" + selected.get() + "\n"
    f.write(linha) 
    f.close()

def movimentos():
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
    windowMovimentos.configure(menu = menu, background="lightblue") # ADICIONA O MENU A PÁGINA(WINDOW)
    

    # ---------- INTERFACE --------------
    global num
    num = IntVar()
    lblNumEstudante = Label(windowMovimentos, text="Número do estudante: ", bg="lightblue")
    lblNumEstudante.place(x=30, y= 30)
    entryNumEstudante = Entry(windowMovimentos, width=20, textvariable = num)
    entryNumEstudante.place(x=170, y=33)

    frameMovimentos = LabelFrame(windowMovimentos, text=" Movimentos ", width= 200, height=150, bg="lightblue")
    frameMovimentos.place(x=30, y=150)

    global selected
    selected = StringVar()
    rdEntrada = Radiobutton(windowMovimentos, text="Entrada", value="Entrada", variable= selected, bg="lightblue")
    rdEntrada.place(x=50, y=180)
    rdSaida = Radiobutton(windowMovimentos, text="Saida", value="Saida", variable= selected, bg="lightblue")
    rdSaida.place(x=50, y=230)
    selected.set("Entrada")

    btnRegistro = Button(windowMovimentos, text="Registrar", command=lambda:registro(num,selected), width=20, height=5)
    btnRegistro.place(x=290, y=190)

    lblHistorico = Label(windowMovimentos, text="Histórico de movimentos", bg="lightblue")
    lblHistorico.place(x=600, y=120)
    infoMovimentos = Text(windowMovimentos, wrap=None, width=35, height=20)
    infoMovimentos.place(x=550, y=150)



    



    

def goBack(window):
    window.destroy()
    mainWindow.deiconify() #restaura a janela anterior




# ---------- GUI MAIN WINDOW --------------

mainWindow = Tk()
mainWindow.geometry("800x500")
mainWindow.title("Ex 01 - Gerir presenças")
mainWindow.resizable(0,0)

screenWidth = mainWindow.winfo_screenwidth()
screenHeight = mainWindow.winfo_screenheight()

appWidth = 1000
appHeight = 500

x = (screenWidth/2) - (appWidth/2)
y = (screenHeight/2) - (appHeight/2)
mainWindow.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')

            # ---------- MENU --------------
menuBar = Menu(mainWindow)   #CRIA O MENU

menuBar.add_command(label = "Movimentos", command = movimentos)  # ADICIONA CADA BOTAO/COMANDO AO MENU
menuBar.add_command(label = "Consulta", command = None)
menuBar.add_command(label = "Sair", command = mainWindow.quit)

mainWindow.configure(menu = menuBar, background="lightblue") # ADICIONA O MENU A PÁGINA(WINDOW)

            # --------- CONTENT --------------
imgPrincipal = PhotoImage(file = ".//ficha12//images//img-gestao.png")
labelImgPrincipal = Label(mainWindow, image=imgPrincipal, width = 600)
labelImgPrincipal.place(x=0, y=0)

titulo = Label(mainWindow, text="Gestor de presenças", bg="lightblue", font=14)
titulo.place(x=700, y= 230)


mainWindow.mainloop()