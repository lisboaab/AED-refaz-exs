from tkinter import *
from tkinter import filedialog


window = Tk()
window.geometry("1000x500") #(width x height) em px
window.title("Tests Setup")
window.resizable(0,0) #colocar 1 se quiser a opcao de redimensionar

screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()

appWidth = 1000 #colocar a width e height do app
appHeight = 500

x = (screenWidth/2) - (appWidth/2)
y = (screenHeight/2) - (appHeight/2)
window.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')

#---------------FUNCOES------------------
def selectFile():
    """Altera imagem"""
    global imagem1
    global selected_image
    selected_image = filedialog.askopenfilename(title="Selecione uma imagem", initialdir=".//imagens",
                filetypes= (("png files", "*.png"),("all files", "*.*")))
    imagem1 = PhotoImage(file = selected_image)
    canvaImg.itemconfig(img1, image=imagem1)

def guardarImg():
    global selected_image
    file = ".//testes anteriores//normal20-21//ficheiros//setup.txt"
    f = open(file, "w", encoding="utf-8")
    f.write(selected_image)
    f.close()

def verNotific():
    file = ".//testes anteriores//normal20-21//ficheiros//notificacao.txt"
    f = open(file, "r", encoding="utf-8")
    lista = f.readlines()
    f.close()
    if check5k.get() == 1:
        txtBox.delete("0.0", "end")
        for linha in lista:
            div = linha.split(";")
            prova = div[0]
            info = div[1]
            if prova == "5K":
                txtBox.insert("end", info)
    elif check10k.get() == 1:
        txtBox.delete("0.0", "end")
        for linha in lista:
            div = linha.split(";")
            prova = div[0]
            info = div[1]
            if prova == "10K":
                txtBox.insert("end", info)
    elif check21k.get() == 1:
        txtBox.delete("0.0", "end")
        for linha in lista:
            div = linha.split(";")
            prova = div[0]
            info = div[1]
            if prova == "21K":
                txtBox.insert("end", info)
    """elif check21k.get() == 1 and check10k.get() == 1 and check5k.get() == 1: #os 3
        txtBox.delete("0.0", "end")
        for linha in lista:
            div = linha.split(";")
            prova = div[0]
            info = div[1]
            txtBox.insert("end", info)
    elif check21k.get() == 1 and check10k.get(): #21 e 10
        txtBox.delete("0.0", "end")
        for linha in lista:
            div = linha.split(";")
            prova = div[0]
            info = div[1]
            if prova == "21K" or prova == "10K":
                txtBox.insert("end", info)
    elif check21k.get() == 1 and check5k.get(): #21 e 5
        txtBox.delete("0.0", "end")
        for linha in lista:
            div = linha.split(";")
            prova = div[0]
            info = div[1]
            if prova == "21K" or prova == "5K":
                txtBox.insert("end", info)
    elif check5k.get() == 1 and check10k.get(): #5 e 10
        txtBox.delete("0.0", "end")
        for linha in lista:
            div = linha.split(";")
            prova = div[0]
            info = div[1]
            if prova == "5K" or prova == "10K":
                txtBox.insert("end", info)"""

#---------------GUI------------------
#Frame 1
frameImg = LabelFrame(window, width=300, height=400)
frameImg.place(x=15, y=15)

labelTitulo = Label(frameImg, text="As minhas provas")
labelTitulo.place(x=30, y=20)

lblLogotipo = Label(frameImg, text="Logotipo da Prova: ")
lblLogotipo.place(x=10, y=100)
btnLogotipo = Button(frameImg, text="Selecionar", width=15, command=selectFile)
btnLogotipo.place(x= 120, y=100)

canvaImg = Canvas(frameImg, width=200, height=150, bd=2, relief=SUNKEN)
canvaImg.place(x=20,y=170)

img = PhotoImage(file = ".//testes anteriores//normal21-22//imagens//pesquisar.png")
img1 = canvaImg.create_image(0,0, anchor=NW, image=img)

btnGuardar = Button(frameImg, text="Guardar", command=guardarImg, width=15)
btnGuardar.place(x=50, y=350)

#Frame 2
frameInfo = LabelFrame(window, width=500, height=400)
frameInfo.place(x=400, y=15)

labelTitulo = Label(frameInfo, text="As minhas notificações")
labelTitulo.place(x=30, y=20)

frameNotific = LabelFrame(frameInfo, text="Ver notificações de: ", width=300, height=100)
frameNotific.place(x=20, y=70)

check5k = IntVar()
check10k = IntVar()
check21k = IntVar()
check10k.set(1) 

check01 = Checkbutton(frameNotific, text="5K", variable = check5k)  # uma variavel exclusiva pra cada botao
check02 = Checkbutton(frameNotific, text="10K", variable = check10k)
check03 = Checkbutton(frameNotific, text="21K", variable = check21k)
check01.place(x=20, y=20)
check02.place(x=80, y=20)
check03.place(x=140, y=20)

btnVer = Button(frameInfo, text="Ver", width=40, command=verNotific)
btnVer.place(x=20,y=180)

txtBox = Text(frameInfo, width=55, height=9)
txtBox.place(x=20,y=230)

window.mainloop()