from tkinter import *
from tkinter import filedialog
import os
import random
from tkinter import messagebox


window = Tk()
window.geometry("1000x500") #(width x height) em px
window.title("ficha 14")
window.resizable(0,0) #colocar 1 se quiser a opcao de redimensionar

screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()

appWidth = 1000 #colocar a width e height do app
appHeight = 500

x = (screenWidth/2) - (appWidth/2)
y = (screenHeight/2) - (appHeight/2)
window.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')

#---------------FUNCOES------------------
fileAvatar = ".//ficha14//ficheiros//perfil.txt"
fileProvas = ".//ficha14//ficheiros//provas.txt"
fileUtilizadores = ".//ficha14//ficheiros//utilizadores.txt"

def novoJogo():
    print()

def mudaImagem():
    """Altera imagem avatar"""
    global imgCreate
    global imagem1
    global filename
    filename = filedialog.askopenfilename(title="Selecione uma imagem", initialdir=".//imagens",
                filetypes= (("png files", "*.png"),("all files", "*.*")))
    imagem1 = PhotoImage(file = filename)
    canvaImg.itemconfig(imgCreate, image=imagem1)

    

def guardarConfiguracoes():
    """Pega path da imagem selecionada e o botao que clicou e salva num arquivo separado pro canvas pegar a info de lá"""
    global selected 
    global filename
    continente = selected.get()

    
    if not os.path.exists(fileAvatar):
        f = open(fileAvatar, "x")
        f.close()
    else: 
        f = open(fileAvatar, "w", encoding="utf-8")
        f.write(filename + ";" + continente)
        f.close()

def configuracoes():
    """Painel onde vai aparecer as coisas pra mudar a info"""

    painelConfig = PanedWindow(window, width = 850, height = 300, relief = "sunken")
    painelConfig.place(x=0, y=150) 

    global imgCreate
    imgVar = attAvatar()
    imgLogin = PhotoImage(file= imgVar)
    canvaImg = Canvas(painelConfig, width=100, height=100)
    canvaImg.place(x=100,y=20)
    imgCreate = canvaImg.create_image(10, 10, image=imgLogin, anchor=NW)
    

    btnImg = Button(painelConfig, width=15,height=4, text="Selecione imagem \n de perfil", command=mudaImagem)
    btnImg.place(x=50, y=20)

    global selected
    selected= StringVar()
    frameCont = LabelFrame(painelConfig, text="Selecione um continente para jogar: ", width=500, height=150)
    frameCont.place(x=20, y=150)
    rdbEuropa = Radiobutton(frameCont, value="Europa",text="Europa", variable=selected)
    rdbAmerica = Radiobutton(frameCont, value="America",text="America",  variable=selected)
    rdbAsia = Radiobutton(frameCont, value="Asia", text="Asia", variable=selected)
    rdbEuropa.place(x=10, y= 20)
    rdbAmerica.place(x=10, y=40)
    rdbAsia.place(x=10, y=60)

    btnGuardar = Button(painelConfig, text="Guardar configuracoes", width=20, height=2, command=guardarConfiguracoes)
    btnGuardar.place(x=570, y=200)

def attAvatar():
    """
    Lê arquivo txt e coloca a imagem do avatar na main window"""
    f = open(fileAvatar, "r", encoding="utf-8")
    linha = f.readline()
    f.close()
    div = linha.split(";")
    imagemAvatar = div[0]
    img = str(imagemAvatar)
    return img

def sortearCidade():
    global entryCidade
    entryCidade.configure(state="normal")
    f = open(fileAvatar, "r", encoding="utf-8")
    linha = f.readline()
    f.close()
    div = linha.split(";")
    continente = div[1]
    
    fileParaAbrir = ".//ficha14//ficheiros//" + continente + ".txt"

    file = open(fileParaAbrir, "r", encoding="utf-8")
    lista = file.readlines()
    file.close
    indice_aleatorio = random.randint(0, len(lista)-1)
    cidade =  lista[indice_aleatorio]

    global city
    global op1
    global op2
    global op3
    global op4
    global respostaCerta

    print(cidade)
    div = cidade.split(";")
    city = div[0]
    op1 = div[1]
    op2 = div[2]
    op3 = div[3]
    op4 = div[4]
    respostaCerta = div[5]
    entryCidade.insert(0, city)

    entryCidade.configure(state="readonly")

def validacao():
    global selected
    global respostaCerta
    countAcertos = 0
    countErros = 0
    selecao = selected.get()
    if selecao == respostaCerta:
        messagebox.showinfo(title="Sua resposta está: ", message="CORRETA!!         ")
        countAcertos += 1
    else:
        messagebox.showinfo(title="Sua resposta está: ", message="INCORRETA!!          ")
        countErros += 1




def painelNovoJogo():
    """Painel de novo jogo"""

    painelNovoJogo = PanedWindow(window, width = 850, height = 300, relief = "sunken")
    painelNovoJogo.place(x=0, y=150) 

    global entryCidade
    lblCidade = Label(painelNovoJogo, text="Cidade")
    lblCidade.place(x=300, y=20)
    entryCidade = Entry(painelNovoJogo, width=25)
    entryCidade.place(x=250, y= 50)

    global city
    global op1
    global op2
    global op3
    global op4
    global respostaCerta
    sortearCidade()

    global selected
    selected = StringVar()
    frameAdivinha = LabelFrame(painelNovoJogo, text="É a capital do país: ", width=500, height=100)
    frameAdivinha.place(x= 60, y= 100)
    rdbOp1 = Radiobutton(frameAdivinha, text=op1, variable=selected, value=op1)
    rdbOp2 = Radiobutton(frameAdivinha, text=op2, variable=selected, value=op2)
    rdbOp3 = Radiobutton(frameAdivinha, text=op3, variable=selected, value=op3)
    rdbOp4 = Radiobutton(frameAdivinha, text=op4, variable=selected, value=op4)
    rdbOp1.place(x=20, y=20)
    rdbOp2.place(x=20, y=50)
    rdbOp3.place(x=200, y=20)
    rdbOp4.place(x=200, y=50)

    btnNovaPergunta = Button(painelNovoJogo, text="Nova Pergunta", width=15, command=sortearCidade)
    btnNovaPergunta.place(x=60, y=250)
    btnValidacao = Button(painelNovoJogo, text="Validar Resposta", width=15, command=validacao)
    btnValidacao.place(x=200, y=250)






#---------------GUI------------------
btnNovoJogo = Button(window, text="Novo jogo", width=15, height=3, command=painelNovoJogo)
btnNovoJogo.place(x=50, y=10)
btnFechar = Button(window, text="Fechar", width=15, height=3, command=window.quit)
btnFechar.place(x=200, y=10)
btnConfig = Button(window, text="Configurações", width=15, height=3, command=configuracoes)
btnConfig.place(x=350, y=10)

imgVar = attAvatar()
imgLogin = PhotoImage(file=imgVar)
canvaImg = Canvas(window, width=100, height=100)
canvaImg.create_image(10, 10, image=imgLogin, anchor=NW)
canvaImg.place(x=500, y=10)

window.mainloop()