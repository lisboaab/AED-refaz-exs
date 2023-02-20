from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog

window = Tk()
window.geometry("1000x500") #(width x height) em px
window.title("Talks")
window.resizable(0,0) #colocar 1 se quiser a opcao de redimensionar

screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()

appWidth = 1000 #colocar a width e height do app
appHeight = 500

x = (screenWidth/2) - (appWidth/2)
y = (screenHeight/2) - (appHeight/2)
window.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')


#-------------FUNCOES---------------------

def mudaImagem():
    """Altera imagem"""
    global imagem1
    filename = filedialog.askopenfilename(title="Selecione uma imagem", initialdir=".//imagens",
                filetypes= (("png files", "*.png"),("jpg files", "*.jpg")))
    imagem1 = PhotoImage(file = filename)
    canvaImg.itemconfig(img1, image=imagem1)

def lerficheiro():
    
    file = ".//testes anteriores//rec20-21//ficheiros//inscricoes.txt"
    f = open(file, "r", encoding="utf-8")
    lista= f.readlines()
    f.close()
    tree.delete(*tree.get_children())
    for linha in lista:
        campos = linha.split(";")
        tree.insert("", "end", values=(campos[0], campos[1]))
    doc = 0
    stu = 0
    ext = 0
    for linha in lista:
        campos = linha.split(";")
        nome = campos[0]
        perfil = campos[1]
        if perfil == "Estudante":
            stu +=1
        elif perfil == "Docente":
            doc += 1
        elif perfil == "Externo":
            ext += 1
    """doc1 = str(doc)
    stu1 = str(stu)
    ext1 = str(ext) """
    linha = f"{doc} docentes, {stu} estudantes, {ext} externos"
    messagebox.showinfo("Informação", linha)
    conta = len(tree.get_children())
    entryNumInsc.delete(0, END) 
    entryNumInsc.insert(0, str(conta))

def adicionar():
    if name.get() == "":
        messagebox.showwarning("Inscrição", "Insira um nome para a inscrição")
    else:
        nome = name.get()
        perfil = selected.get()
        info = [nome, perfil]
        tree.insert("", "end", values=info)
    conta = len(tree.get_children())
    entryNumInsc.delete(0, END) 
    entryNumInsc.insert(0, str(conta))


def guardar():
    ficheiro = ".//testes anteriores//rec20-21//ficheiros//inscricoes.txt"
    f = open(ficheiro, "w", encoding="utf-8")
    for i in tree.get_children():
        valores = tree.item(i)["values"]
        f.write(f"{valores[0]};{valores[1]};\n")
    f.close()






#-------------GUI---------------------
# Inscricao
name = StringVar()
lblNome = Label(window, text="Nome:")
entryNome = Entry(window, width=15, textvariable=name)
lblNome.place(x=20, y= 20)
entryNome.place(x=78, y=22)

frameInscricao = LabelFrame(window, text="Tipo Inscrição: ", width=200, height=200)
frameInscricao.place(x=20, y= 80)

selected = StringVar()
rdbtnDoc = Radiobutton(frameInscricao, text="Docente", value="Docente", variable=selected)
rdbtnStud = Radiobutton(frameInscricao, text="Estudante", value="Estudante", variable=selected)
rdbtnExt = Radiobutton(frameInscricao, text="Externo", value="Externo", variable=selected)
rdbtnDoc.place(x=15, y=30)
rdbtnStud.place(x=15, y=80)
rdbtnExt.place(x=15, y=130)

# Treeview
frameTree = LabelFrame(window, width=400, height=201)
frameTree.place(x=300, y= 80)
tree = ttk.Treeview(frameTree, selectmode= "browse", columns = ("Nome", "Perfil"), show = "headings")
tree.place(x= 10, y= 10)
tree.column("Nome", width= 210 , anchor = W)
tree.heading("Nome", text ="Nome")
tree.column("Perfil", width= 160 , anchor = CENTER) 
tree.heading("Perfil", text ="Perfil")

# Botoes
btnLerFile = Button(window, text="Ler ficheiro", width=15, command=lerficheiro)
btnAdicionar = Button(window, text="Adicionar", width=15, command=adicionar)
btnGuardar = Button(window, text="Guardar", width=15, command=guardar)
btnLerFile.place(x=20, y=300)
btnAdicionar.place(x=150, y=300)
btnGuardar.place(x=280, y=300)

# Numero inscricoes
lblNumInscricoes = Label (window, text="Nº de inscrições: ")
lblNumInscricoes.place(x=420, y=300)
numInsc = IntVar()
entryNumInsc = Entry(window, textvariable=numInsc)
entryNumInsc.place(x=520, y=301)

# Imagem
canvaImg = Canvas(window, width=200, height=150, bd=2, relief=SUNKEN)
canvaImg.place(x=750,y=100)

img = PhotoImage(file = ".//testes anteriores//normal21-22//imagens//pesquisar.png")
img1 = canvaImg.create_image(0,0, anchor=NW, image=img)

btnImg = Button(window, width=15, text="Mudar Imagem", command=mudaImagem)
btnImg.place(x=750, y=40)

window.mainloop()