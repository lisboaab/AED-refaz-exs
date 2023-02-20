from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog

window = Tk()
window.geometry("1000x500") #(width x height) em px
window.title("Filmes Dashboard")
window.resizable(0,0) #colocar 1 se quiser a opcao de redimensionar

screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()

appWidth = 1000 #colocar a width e height do app
appHeight = 500

x = (screenWidth/2) - (appWidth/2)
y = (screenHeight/2) - (appHeight/2)
window.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')

#---------------FUNCOES------------------
def seeInTreeview():
    cat =""
    pos = listBoxCategorias.curselection()
    if pos == (0,):
        cat = "Drama"
    elif pos == (1,):
        cat = "Comédia"
    elif pos == (2,):
        cat = "Thriller"
    elif pos == (3,):
        cat = "Animação"
    elif pos == (4,):
        cat = "Ação"
    elif pos == (5,):
        cat = "Terror"

    file = ".//testes anteriores//teste2-20-21//ficheiros//filmes.txt"
    f = open(file, "r", encoding="utf-8")
    lista = f.readlines()
    f.close()
    tree.delete(*tree.get_children())
    
    for linha in lista:
        div = linha.strip().split(";")    
        if div[0] == cat:
            tree.insert("", "end", values=(div[1], div[2]))


def addFilme():
    titulo = adcFilme.get()
    visualizacoes = str(addVisu.get())
    cat =""
    pos = listBoxCategorias.curselection()
    if pos == (0,):
        cat = "Drama"
    elif pos == (1,):
        cat = "Comédia"
    elif pos == (2,):
        cat = "Thriller"
    elif pos == (3,):
        cat = "Animação"
    elif pos == (4,):
        cat = "Ação"
    elif pos == (5,):
        cat = "Terror"
    
    linha = cat + ";" + titulo + ";" + visualizacoes + ";\n"
    file = ".//testes anteriores//teste2-20-21//ficheiros//filmes.txt"
    f = open(file, "a", encoding="utf-8")
    f.write(linha)
    f.close()

def verMais():
    conta = len(tree.get_children())
    entryNfilme.delete(0, END)  # Limpa o valor atual do widget Entry
    entryNfilme.insert(0, str(conta))

    ficheiro = ".//testes anteriores//teste2-20-21//ficheiros//filmes.txt"
    f = open(ficheiro, "r", encoding="utf-8")
    lista = f.readlines()
    f.close()

    cat =""
    pos = listBoxCategorias.curselection()
    if pos == (0,):
        cat = "Drama"
    elif pos == (1,):
        cat = "Comédia"
    elif pos == (2,):
        cat = "Thriller"
    elif pos == (3,):
        cat = "Animação"
    elif pos == (4,):
        cat = "Ação"
    elif pos == (5,):
        cat = "Terror"
    
    filmeMaisVisto = None
    maiorVisu = 0
    for linha in lista:
        div = linha.strip().split(";")
        if div[0] == cat:
            visu = int(div[2])
            if visu > maiorVisu:
                filmeMaisVisto = div[1]
                maiorVisu = visu
    
    entryFilmeMaisVisto.delete("0", END)
    entryFilmeMaisVisto.insert("0", filmeMaisVisto)

def mudaImagem():
    """Altera imagem"""
    global imagem1
    filename = filedialog.askopenfilename(title="Selecione uma imagem", initialdir=".//imagens",
                filetypes= (("png files", "*.png"),("all files", "*.*")))
    imagem1 = PhotoImage(file = filename)
    canvaImg.itemconfig(img1, image=imagem1)


#---------------GUI------------------
# categorias
lblCategorias = Label(window, text="Categorias", font=("Helvetica", 11))
lblCategorias.place(x=20,y=20)
listBoxCategorias = Listbox(window, width=25, height=15, border=2)
listBoxCategorias.place(x=20, y=60)
ficheiro = ".//testes anteriores//teste2-20-21//ficheiros//categorias.txt"
f = open(ficheiro, "r", encoding="utf-8")
lista = f.readlines()
f.close()
for i in lista:
    listBoxCategorias.insert(END, i)

btnTree = Button(window, text=">", width=4, command=seeInTreeview)
btnTree.place(x=190, y=160)

# treeview
tree = ttk.Treeview(window, selectmode= "browse", columns = ("Filme", "Visualizacoes"), show = "headings")
tree.place(x= 260, y= 60)
tree.column("Filme", width= 300 , anchor = W) # c - centro; e -  direita; w - esquerda
tree.heading("Filme", text ="Filme")
tree.column("Visualizacoes", width= 150 , anchor = CENTER) # c - centro; e -  direita; w - esquerda
tree.heading("Visualizacoes", text ="Visualizacoes")

#add filmes
adcFilme = StringVar()
addVisu = IntVar()

frameAddFilme = LabelFrame(window, width=200, height=250)
frameAddFilme.place(x=750, y=60)
lblFilme= Label(frameAddFilme, text="Filme:")
lblFilme.place(x=10, y=20)
entryFilme = Entry(frameAddFilme, width=15, textvariable=adcFilme)
entryFilme.place(x=10, y=50)
lblVisu= Label(frameAddFilme, text="Visualizações:")
lblVisu.place(x=10, y=90)
entryVisu = Entry(frameAddFilme, width=15, textvariable=addVisu)
entryVisu.place(x=10, y=120)

btnAddFilme = Button(frameAddFilme, text="Adicionar filme", width=15, command=addFilme)
btnAddFilme.place(x=10, y= 160)

btnARefresh = Button(frameAddFilme, text="Refresh Vista", width=15, command=seeInTreeview)
btnARefresh.place(x=10, y= 200)

# ver categorias
frameCategorias = LabelFrame(window, width=500, height=120)
frameCategorias.place(x=20, y= 350)

btnVerCat = Button(frameCategorias, text="Categoria|Ver +", width=16, height=3, command=verMais)
btnVerCat.place(x=30, y=30)

qtyFilmes = IntVar()
filmeMaisVisto = StringVar()
lblNumFilmes = Label(frameCategorias, text="Nº filmes:")
lblNumFilmes.place(x=180, y=30)
entryNfilme= Entry(frameCategorias, width=15, textvariable=qtyFilmes)
entryNfilme.place(x=250,y=30)
lblFilmeMaisVisto = Label(frameCategorias, text="Filme + visto:")
lblFilmeMaisVisto.place(x=180, y=70)
entryFilmeMaisVisto= Entry(frameCategorias, width=15, textvariable=filmeMaisVisto)
entryFilmeMaisVisto.place(x=270,y=70)

# canvas
canvaImg = Canvas(window, width=200, height=150, bd=2, relief=SUNKEN)
canvaImg.place(x=720,y=320)

img = PhotoImage(file = ".//testes anteriores//normal21-22//imagens//pesquisar.png")
img1 = canvaImg.create_image(0,0, anchor=NW, image=img)

btnImg = Button(window, width=15, text="Selecionar Imagem", command=mudaImagem)
btnImg.place(x=850, y=450)


window.mainloop()