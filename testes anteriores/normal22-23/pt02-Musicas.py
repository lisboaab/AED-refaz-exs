from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog

window = Tk()
window.geometry("1000x500") #(width x height) em px
window.title("Músicas Dashboard")
window.resizable(0,0) #colocar 1 se quiser a opcao de redimensionar

screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()

appWidth = 1000 #colocar a width e height do app
appHeight = 500

x = (screenWidth/2) - (appWidth/2)
y = (screenHeight/2) - (appHeight/2)
window.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')

#---------------FUNCOES------------------
fBandas = ".//testes anteriores//normal22-23//ficheiros//bandas.txt"
fMusicas = ".//testes anteriores//normal22-23//ficheiros//musicas.txt"

def seeInTreeview():
    cat =""
    pos = listBoxBandas.curselection()
    if pos == (0,):
        cat = "Harry Styles"
    elif pos == (1,):
        cat = "Coldplay"
    elif pos == (2,):
        cat = "Maverick City"

    f = open(fMusicas, "r", encoding="utf-8")
    lista = f.readlines()
    f.close()
    tree.delete(*tree.get_children())
    
    visu = 0
    visuN = ""
    for linha in lista:
        div = linha.strip().split(";")    
        if div[0] == cat:
            visualizacoes = div[2] 
            if int(visualizacoes) >= 1000000:
                visu = (int(visualizacoes)/1000000)
                visuN = str(visu) + "M"
            elif int(visualizacoes) >= 1000:
                visu = (int(visualizacoes)/1000)
                visuN = str(visu) + "m"
            tree.insert("", "end", values=(div[1], visuN))


def addMusica():
    titulo = adcMusica.get()
    visualizacoes = addVisu.get()

    
    cat =""
    pos = listBoxBandas.curselection()
    if pos == (0,):
        cat = "Harry Styles"
    elif pos == (1,):
        cat = "Coldplay"
    elif pos == (2,):
        cat = "Maverick City"

    linha = cat + ";" + titulo + ";" + str(visualizacoes) + "; ;\n"
    f = open(fMusicas, "a", encoding="utf-8")
    f.write(linha)
    f.close()

def verMais():
    entryNormal()
    conta = len(tree.get_children())
    entryNmsc.delete(0, END)  # Limpa o valor atual do widget Entry
    entryNmsc.insert(0, str(conta))

    f = open(fMusicas, "r", encoding="utf-8")
    lista = f.readlines()
    f.close()

    band = ""
    pos = listBoxBandas.curselection()
    if pos == (0,):
        band = "Harry Styles"
    elif pos == (1,):
        band = "Coldplay"
    elif pos == (2,):
        band = "Maverick City"

    mscMaisVista = None
    maiorVisu = 0
    for linha in lista:
        div = linha.strip().split(";")
        if div[0] == band:
            visu = int(div[2])
            if visu > maiorVisu:
                mscMaisVista = div[1]
                linkYtb = div[3]
                maiorVisu = visu

    
    entryMusicaMaisVista.delete("0", END)
    entryMusicaMaisVista.insert("0", mscMaisVista)
    entryLinkYtb.delete("0", END)
    entryLinkYtb.insert("0", linkYtb)
    entryReadOnly()
    

def mudaImagem():
    """Altera imagem"""
    global imagem1
    filename = filedialog.askopenfilename(title="Selecione uma imagem", initialdir=".//imagens",
                filetypes= (("png files", "*.png"),("all files", "*.*")))
    imagem1 = PhotoImage(file = filename)
    canvaImg.itemconfig(img1, image=imagem1)

def lerBandas():
    f = open(fBandas, "r", encoding="utf-8")
    lista = f.readlines()
    f.close()
    for i in lista:
        listBoxBandas.insert(END, i)

def entryReadOnly():
    entryNmsc.configure(state="readonly")
    entryMusicaMaisVista.configure(state="readonly")
    entryLinkYtb.configure(state="readonly")

def entryNormal():
    entryNmsc.configure(state="normal")
    entryMusicaMaisVista.configure(state="normal")
    entryLinkYtb.configure(state="normal")

#---------------GUI------------------


# bandas
lblBandas = Label(window, text="Bandas", font=("Helvetica", 11))
lblBandas.place(x=20,y=20)
listBoxBandas = Listbox(window, width=25, height=15, border=2)
listBoxBandas.place(x=20, y=60)
lerBandas()
btnTree = Button(window, text=">", width=4, command=seeInTreeview)
btnTree.place(x=190, y=160)

# treeview
tree = ttk.Treeview(window, selectmode= "browse", columns = ("Músicas", "Visualizacoes"), show = "headings")
tree.place(x= 260, y= 60)
tree.column("Músicas", width= 300 , anchor = W) # c - centro; e -  direita; w - esquerda
tree.heading("Músicas", text ="Música")
tree.column("Visualizacoes", width= 150 , anchor = CENTER) # c - centro; e -  direita; w - esquerda
tree.heading("Visualizacoes", text ="Visualizacoes")

#add musicas
adcMusica = StringVar()
addVisu = IntVar()

frameAddMsc = LabelFrame(window, width=200, height=250)
frameAddMsc.place(x=750, y=60)
lblMsc= Label(frameAddMsc, text="Música:")
lblMsc.place(x=10, y=20)
entryMsc = Entry(frameAddMsc, width=15, textvariable=adcMusica)
entryMsc.place(x=10, y=50)
lblVisu= Label(frameAddMsc, text="Visualizações:")
lblVisu.place(x=10, y=90)
entryVisu = Entry(frameAddMsc, width=15, textvariable=addVisu)
entryVisu.place(x=10, y=120)


imgPlus = PhotoImage(file = ".//testes anteriores//normal22-23//plus.png")
btnAddMsc = Button(frameAddMsc, text="Adicionar\nmúsica", image=imgPlus, width=80, height=80, compound="top", command=addMusica)
btnAddMsc.place(x=5, y= 150)

imgRefresh = PhotoImage(file = ".//testes anteriores//normal22-23//refresh.png")
btnARefresh = Button(frameAddMsc, text="Refresh Vista", image=imgRefresh, width=80, height=80, compound="top", command=seeInTreeview)
btnARefresh.place(x=100, y= 150)

# ver musicas
frameMscs = LabelFrame(window, width=500, height=120)
frameMscs.place(x=20, y= 350)

imgVermais = PhotoImage(file = ".//testes anteriores//normal22-23//music-info.png")
btnVerCat = Button(frameMscs, image=imgVermais , width=70, height=70, command=verMais)
btnVerCat.place(x=30, y=30)

qtyMusicas = IntVar()
mscMaisVista = StringVar()
linkYtb = StringVar()
lblNumMscs = Label(frameMscs, text="Nº músicas:")
lblNumMscs.place(x=180, y=20)
entryNmsc= Entry(frameMscs, width=15, textvariable=qtyMusicas)
entryNmsc.place(x=250,y=20)
lblMusicaMaisVista = Label(frameMscs, text="Música + vista:")
lblMusicaMaisVista.place(x=180, y=50)
entryMusicaMaisVista= Entry(frameMscs, width=15, textvariable=mscMaisVista)
entryMusicaMaisVista.place(x=270,y=50)
lblLinkYtb = Label(frameMscs, text="Link youtube: ")
lblLinkYtb.place(x=180, y=80)
entryLinkYtb= Entry(frameMscs, width=15, textvariable=linkYtb)
entryLinkYtb.place(x=270,y=80)


# canvas
canvaImg = Canvas(window, width=200, height=150, bd=2, relief=SUNKEN)
canvaImg.place(x=720,y=320)

img = PhotoImage(file = ".//testes anteriores//normal21-22//imagens//pesquisar.png")
img1 = canvaImg.create_image(0,0, anchor=NW, image=img)

btnImg = Button(window, width=15, text="Selecionar Imagem", command=mudaImagem)
btnImg.place(x=850, y=450)


window.mainloop()