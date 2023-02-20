from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry("1000x500") #(width x height) em px
window.title("Running Tool Management")
window.resizable(0,0) #colocar 1 se quiser a opcao de redimensionar

screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()

appWidth = 1000 #colocar a width e height do app
appHeight = 500

x = (screenWidth/2) - (appWidth/2)
y = (screenHeight/2) - (appHeight/2)
window.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')

#---------------FUNCOES------------------

def passTreeview():
    pos = lboxAtv.curselection()
    file = ".//testes anteriores//normal20-21//ficheiros//tempos.txt"
    f = open(file, "r")
    lista = f.readlines()
    f.close()
    pos= str(pos[0])
    tree.delete(*tree.get_children())
    for linha in lista:
        div = linha.strip().split(";")
        if div[0] == pos:
            tree.insert("", "end", values=(div[1], div[2], div[3]))

def infoTreeview():
    """Mostra quantas atvs estão sendo mostradas na treeview e qual o melhor tempo delas"""
    #conta
    conta = len(tree.get_children())
    entryNumProvas.delete(0, END)  # Limpa o valor atual do widget Entry
    entryNumProvas.insert(0, str(conta)) #Adiciona valor novo
    #tempo
    mTempo = float('inf')
    for i in tree.get_children():
        tempo = float(tree.item(i)["values"][2])
        if tempo < mTempo:
            mTempo = tempo
    entryMelhorTempo.delete(0, END)
    entryMelhorTempo.insert(0, str(mTempo))



def filtrar():
    nome = filtrarPalavra.get()
    file = ".//testes anteriores//normal20-21//ficheiros//tempos.txt"
    f = open(file, "r")
    lista = f.readlines()
    f.close()
    tree.delete(*tree.get_children())
    for i in lista:
        div = i.split(";")
        prova = div[2]
        if nome == prova:
            tree.insert("", "end", values=(div[1], div[2], div[3]))



#---------------GUI------------------

#Listbox atv
ficheiro = ".//testes anteriores//normal20-21//ficheiros//atividades.txt"
f = open(ficheiro, "r")
lista = f.readlines()
f.close()

lblAtv= Label(window, text="Atividades")
lblAtv.place(x=10, y=20)
lboxAtv = Listbox(window, width=30, height=10)
lboxAtv.place(x=10,y=50)
for i in lista:
    lboxAtv.insert(END, i)

#Botoes
btnPassTree = Button(window, text=">", width=3, command=passTreeview)
btnInfoTree = Button(window, text="+", width=3, command=infoTreeview)
btnPassTree.place(x=200, y= 70)
btnInfoTree.place(x=200, y= 120)
    
# treeview
tree = ttk.Treeview(window, selectmode= "browse", columns = ("Data", "Prova", "Tempo"), show = "headings")
tree.place(x= 400, y= 50)
tree.column("Data", width= 150 , anchor = W) 
tree.heading("Data", text ="Data")
tree.column("Prova", width= 150 , anchor = W) 
tree.heading("Prova", text ="Prova")
tree.column("Tempo", width= 150 , anchor = W) 
tree.heading("Tempo", text ="Tempo")

# numero provas e melhor tempo
numeroProvas = IntVar()
lblNumProvas = Label(window, text="Nº provas: ")
lblNumProvas.place(x=420,y=300)
entryNumProvas = Entry(window, width=10, textvariable=numeroProvas)
entryNumProvas.place(x=500, y=300)

melhorTempo = IntVar()
lblMelhorTempo = Label(window, text="Melhor tempo: ")
lblMelhorTempo.place(x=650,y=300)
entryMelhorTempo = Entry(window, width=10, textvariable=melhorTempo)
entryMelhorTempo.place(x=750, y=300)

#filtrar
filtrarPalavra = StringVar()
frameFiltrar = LabelFrame(window, text="Filtrar ", width=400, height=100)
frameFiltrar.place(x=400, y=350)
lblfiltro = Label(frameFiltrar, text="Prova: ")
lblfiltro.place(x=15, y=20)
entryFiltrar= Entry(frameFiltrar, width=15, textvariable=filtrarPalavra)
entryFiltrar.place(x=70, y=20)
btnFiltrar = Button(frameFiltrar, width=10, text="Filtrar", command=filtrar)
btnFiltrar.place(x=210, y=20)

#canvas
canvaImg = Canvas(window, width=200, height=150, bd=2, relief=SUNKEN)
canvaImg.place(x=20,y=240)

img = PhotoImage(file = ".//testes anteriores//normal21-22//imagens//pesquisar.png")
img1 = canvaImg.create_image(0,0, anchor=NW, image=img)

window.mainloop()