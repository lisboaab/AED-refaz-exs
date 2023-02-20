from tkinter import *
from tkinter import ttk
from tkinter import filedialog

window = Tk()
window.geometry("1000x500") #(width x height) em px
window.title("Trails App")
window.resizable(0,0) #colocar 1 se quiser a opcao de redimensionar

screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()

appWidth = 1000 #colocar a width e height do app
appHeight = 500

x = (screenWidth/2) - (appWidth/2)
y = (screenHeight/2) - (appHeight/2)
window.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')

#-------------FUNCOES------------
def onChecked(checkCurto, checkUltra):
    """Mostra na treeview as atividades em cada tipo de checkbutton"""
    if checkCurto.get() == 1 and checkUltra.get() == 0:
        tree.delete(*tree.get_children())
        file = ".//testes anteriores//normal21-22//ficheiros//trails.txt"
        f = open(file, "r", encoding="utf-8")
        lista= f.readlines()
        f.close()
        for linha in lista:
            campos = linha.split(";")
            tree.insert("", "end", values=(campos[0], campos[1], campos[2]))
    elif checkUltra.get() == 1 and checkCurto.get() == 0:
        tree.delete(*tree.get_children())
        file = ".//testes anteriores//normal21-22//ficheiros//ultratrails.txt"
        f = open(file, "r", encoding="utf-8")
        lista= f.readlines()
        f.close()
        for linha in lista:
            campos = linha.split(";")
            tree.insert("", "end", values=(campos[0], campos[1], campos[2]))
    elif checkUltra.get() == 0 and checkCurto.get() == 0:
        tree.delete(*tree.get_children())
    elif checkUltra.get() == 1 and checkCurto.get() == 1:
        tree.delete(*tree.get_children())
        file1 = ".//testes anteriores//normal21-22//ficheiros//trails.txt"
        f1 = open(file1, "r", encoding="utf-8")
        lista1= f1.readlines()
        f1.close()
        for linha in lista1:
            campos = linha.split(";")
            tree.insert("", "end", values=(campos[0], campos[1], campos[2]))
        
        file2 = ".//testes anteriores//normal21-22//ficheiros//ultratrails.txt"
        f2 = open(file2, "r", encoding="utf-8")
        lista2= f2.readlines()
        f2.close()
        for linha in lista2:
            campos = linha.split(";")
            tree.insert("", "end", values=(campos[0], campos[1], campos[2]))
    conta = len(tree.get_children())
    entryNumProvas.delete(0, END)  # Limpa o valor atual do widget Entry
    entryNumProvas.insert(0, str(conta))  # Insere o novo valor no widget Entry


def sort_column(tree, col, reverse):
    """Ordena colunas"""
    lista = [(tree.set(k, col), k) for k in tree.get_children('')]
    lista.sort(reverse=reverse)

    for index, (val, k) in enumerate(lista):
        tree.move(k, '', index)

def mudaImagem():
    """Altera imagem"""
    global imagem1
    filename = filedialog.askopenfilename(title="Selecione uma imagem", initialdir=".//imagens",
                filetypes= (("png files", "*.png"),("all files", "*.*")))
    imagem1 = PhotoImage(file = filename)
    canvaImg.itemconfig(img1, image=imagem1)

def adcFavorito():
    """Adiciona na lisbox a linha selecionada na treeview"""
    pos = tree.selection()

    for index in pos:
        values = tree.item(index)['values'][0]
        lboxFav.insert('end', values)
    
def removFavorito():
    """Remove linha selecionada da listbox"""
    pos = lboxFav.curselection()
    lboxFav.delete(pos)

def guardaFav():
    """Salva os valores da listbox no arquivo txt "favoritos"""
    values = lboxFav.get(0, 'end')
    with open(".//testes anteriores//normal21-22//ficheiros//favoritos.txt", 'w') as file:
        for value in values:
            file.write(value + '\n')




#Checkbuttons
checkCurto = IntVar()
checkUltra = IntVar()
check01 = Checkbutton(window, text="Trail Curto", variable = checkCurto)
check02 = Checkbutton(window, text="Ultra Trail", variable = checkUltra)
checkCurto.set(1)
check01.place(x=60, y=20)
check02.place(x=170, y=20)

#ImgButtons
imgPesquisa = PhotoImage(file = ".//testes anteriores//normal21-22//imagens//pesquisar.png")
btnPesquisa = Button(window, width=35, height=35, image=imgPesquisa, relief=FLAT, command=lambda:onChecked(checkCurto, checkUltra))
btnPesquisa.place(x=300, y= 10)


imgAsc = PhotoImage(file = ".//testes anteriores//normal21-22//imagens//asc.png")
btnAsc = Button(window, width=35, height=35, image=imgAsc, relief=FLAT, command=lambda:sort_column(tree, 2, False))
btnAsc.place(x=400, y= 15)

imgdesc = PhotoImage(file = ".//testes anteriores//normal21-22//imagens//desc.png")
btndesc = Button(window, width=35, height=35, image=imgdesc, relief=FLAT, command=lambda:sort_column(tree, 2, True))
btndesc.place(x=500, y= 15)

#Treeview
tree = ttk.Treeview(window, selectmode= "browse", columns = ("Prova", "Data", "Local"), show = "headings")
tree.place(x= 60, y= 100)
tree.column("Prova", width=200, anchor=W)
tree.heading("Prova", text="Prova")
tree.column("Data", width=150, anchor=CENTER)
tree.heading("Data", text="Data")
tree.column("Local", width=150, anchor=CENTER)
tree.heading("Local", text="Local")

# Número de provas
lblNumProvas = Label (window, text="Número de provas: ")
lblNumProvas.place(x=80, y=345)
numProvas = IntVar()
entryNumProvas = Entry(window, textvariable=numProvas)
entryNumProvas.place(x=200, y=347)

# Adiconar imagem
canvaImg = Canvas(window, width=200, height=150, bd=2, relief=SUNKEN)
canvaImg.place(x=350,y=340)

img = PhotoImage(file = ".//testes anteriores//normal21-22//imagens//pesquisar.png")
img1 = canvaImg.create_image(0,0, anchor=NW, image=img)

btnImg = Button(window, width=15, text="Mudar Imagem", command=mudaImagem)
btnImg.place(x=200, y=450)


# Favoritos
btnAdcFav = Button(window, text="Adicionar\nFavoritos", width=10, command=adcFavorito)
btnRemovFav = Button(window, text="Remover\nFavoritos", width=10, command=removFavorito)
btnAdcFav.place(x=600, y=150)
btnRemovFav.place(x=600, y=230)

lblFav = Label(window, text="Favoritos", font=("Helvetica", 11))
lblFav.place(x=780, y=30)

ficheiro = ".//testes anteriores//normal21-22//ficheiros//favoritos.txt"
f = open(ficheiro, "r")
lista = f.readlines()
f.close()

lboxFav = Listbox(window, width=40, height=20)
lboxFav.place(x=720,y=100)
for i in lista:
    div = i.split(";")
    lboxFav.insert(END, div[0])

btnGuardarFav = Button(window, text="Guardar  Favorito", command=guardaFav, width=33, height=2)
btnGuardarFav.place(x=720, y=440)



window.mainloop()