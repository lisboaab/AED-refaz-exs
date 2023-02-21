from tkinter import * 
from tkinter import ttk

class Application:
    def __init__(self, master=None):
        pass

window = Tk()
Application(window)
window.title('Trails App')
window.resizable(0,0)
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
appWidth = 1000
appHeight = 500
window.geometry(f'{appWidth}x{appHeight}')

favoritos = []

def ler_ficheiro(ficheiro):
    f = open(ficheiro, 'r', encoding='utf-8')
    lista = f.readlines()
    f.close()
    return lista

def tree_dados():
    global checkVarTrailCurto
    global checkVarUltraTrail
    global tree
    tree.delete(*tree.get_children())
    if checkVarTrailCurto.get() == 1 and checkVarUltraTrail.get() == 0:
        ficheiro = './/testes anteriores//normal21-22//ficheiros//trails.txt'
        lista = ler_ficheiro(ficheiro)
        for linha in lista:
            campos = linha.split(';')
            tree.insert("", "end", values=(campos[0], campos[1], campos[2]))
        conta = len(tree.get_children())
        entry_n_provas.delete(0, END) 
        entry_n_provas.insert(0, str(conta))
    elif checkVarTrailCurto.get() == 0 and checkVarUltraTrail.get() == 1:
        ficheiro = './/testes anteriores//normal21-22//ficheiros//ultratrails.txt'
        lista = ler_ficheiro(ficheiro)
        for linha in lista:
            campos = linha.split(';')
            tree.insert("", "end", values=(campos[0], campos[1], campos[2]))
        conta = len(tree.get_children())
        entry_n_provas.delete(0, END) 
        entry_n_provas.insert(0, str(conta))
    elif checkVarTrailCurto.get() == 1 and checkVarUltraTrail.get() == 1:
        ficheiro_trails = './/testes anteriores//normal21-22//ficheiros//trails.txt'
        ficheiro_ultra = './/testes anteriores//normal21-22//ficheiros//ultratrails.txt'
        lista_trails = ler_ficheiro(ficheiro_trails)
        for linha in lista_trails:
            campos = linha.split(';')
            tree.insert("", "end", values=(campos[0], campos[1], campos[2]))
        lista_ultra = ler_ficheiro(ficheiro_ultra)
        for linha in lista_ultra:
            campos = linha.split(';')
            tree.insert("", "end", values=(campos[0], campos[1], campos[2]))
        conta = len(tree.get_children())
        entry_n_provas.delete(0, END) 
        entry_n_provas.insert(0, str(conta))

def adiciona_favorito():
    global tree
    global favoritos
    row_id = tree.focus()
    linha = tree.item(row_id)
    favoritos.append(linha["values"][0])
    insere_favs_textbox()

def insere_favs_textbox():
    global favoritos
    textbox_favoritos.delete(0, END)
    for favorito in favoritos:
        textbox_favoritos.insert(END, favorito)

def remove_favorito():
    global favoritos
    item_id = textbox_favoritos.curselection()
    favoritos.remove(textbox_favoritos.get(textbox_favoritos.curselection()))
    textbox_favoritos.delete(item_id)

def guardar_favoritos():
    global favoritos
    ficheiro = './/testes anteriores//normal21-22//ficheiros//favoritos.txt'
    f = open(ficheiro, 'w', encoding='utf-8')
    for favorito in favoritos:
        f.write(favorito + '\n')
    f.close()


# - - - - - GUI - - - - - #

checkVarTrailCurto = IntVar()
checkVarTrailCurto.set(1)
cb_trail_curto = Checkbutton(window, text="Trail curto", variable=checkVarTrailCurto, command=tree_dados)
cb_trail_curto.place(x=10, y=10)

checkVarUltraTrail = IntVar()
checkVarUltraTrail.set(0)
cb_ultra_trail = Checkbutton(window, text="Ultra trail", variable=checkVarUltraTrail, command=tree_dados)
cb_ultra_trail.place(x=140, y=10)

btn_pesquisar = Button(window, width=4, height=2)
btn_pesquisar.place(x=300, y=10)

btn_asc = Button(window, width=4, height=2)
btn_asc.place(x=360, y=10)

btn_desc = Button(window, width=4, height=2)
btn_desc.place(x=420, y=10)

global tree 
tree = ttk.Treeview(window, selectmode="browse", columns=("Prova","Data","Local"), show="headings")
tree.column("Prova", width=200, anchor="c") # c - center, e - direita, w - esquerda
tree.column("Data", width=100, anchor="c")
tree.column("Local", width=200, anchor="c")
tree.heading("Prova", text="Prova")
tree.heading("Data", text="Data")
tree.heading("Local", text="Local")
tree.place(x=10, y=60)

btn_add_favoritos = Button(window, text="Adicionar Favoritos", command=adiciona_favorito)
btn_add_favoritos.place(x=540, y=120)

btn_remover_favoritos = Button(window, text="Remover Favoritos", command=remove_favorito)
btn_remover_favoritos.place(x=540, y=180)

label_n_provas = Label(text="No de Provas")
label_n_provas.place(x=50, y=300)

entry_n_provas = Entry(window, width=5)
entry_n_provas.place(x=130, y=300)

btn_selecionar_img = Button(window, text="Selecionar imagem", width=20, height=2)
btn_selecionar_img.place(x=60, y=400)

ctn_image = Canvas(window, width=250, height=150, bd=2, relief="sunken")
ctn_image.place(x=255, y=300)

favs_frame = Frame(window, width=300, height=500, relief='sunken', bd=2)
favs_frame.place(x=700, y=0)

label_favoritos = Label(favs_frame, text="Favoritos", font=('Helvetica', 11))
label_favoritos.place(x=120, y=40)

textbox_favoritos = Listbox(favs_frame, width=34, height=15)
textbox_favoritos.place(x=50, y=70)

btn_guardar_favoritos = Button(favs_frame, width=20, height=2, text="Guardar favoritos", command=guardar_favoritos)
btn_guardar_favoritos.place(x=80, y=340)

tree_dados()

window.mainloop()