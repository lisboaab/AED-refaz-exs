from tkinter import * 
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

class Application:
    def __init__(self, master=None):
        pass

window = Tk()
Application(window)
window.title('WebDev Tech Talks')
window.resizable(0,0)
window.geometry('1080x600')

# - - - - - - - GUI - - - -  - - -#

label_nome = Label(window, text="Nome")
label_nome.place(x=20, y=10)

name = StringVar()
name_entry = Entry(window, width=20, textvariable=name)
name_entry.place(x=70, y=10)

# FIRST ROW

frame_tipo_insc = LabelFrame(text="Tipo Inscrição", width=250, height=400)
frame_tipo_insc.place(x=20, y=80)

selected = StringVar()
rd1 = Radiobutton(frame_tipo_insc, text="Docente", value="Docente", variable=selected)
rd2 = Radiobutton(frame_tipo_insc, text="Estudante", value="Estudante", variable=selected)
rd3 = Radiobutton(frame_tipo_insc, text="Externo", value="Externo", variable=selected)
rd1.place(x=10, y=20)
rd2.place(x=10, y=60)
rd3.place(x=10, y=100)

def adicionar_inscricao():
    if name.get() == '':
        messagebox.showerror(title='Impossível adicionar inscrição', message='Não inseriu nome na inscrição')
    else:
        f = open('inscricoes.txt', 'a', encoding='utf-8')
        line = '\n' + name.get() + ';' + selected.get() + ';'
        f.write(line)
        messagebox.showinfo(title='Inscrição adicionada', message='Inscrição adicionada com sucesso')


# SECOND ROW - TREEVIEW

frame_tree = LabelFrame(width=400, height=400, bd=3, relief="sunken")
frame_tree.place(x=300, y=80)

tree = ttk.Treeview(frame_tree, selectmode="browse", columns=("Nome", "Perfil"), show="headings")
tree.place(x=0, y=0)

tree.column("Nome", width=200, anchor="c")
tree.column("Perfil", width=200, anchor="c")
tree.heading("Nome", text="Nome")
tree.heading("Perfil", text="Perfil")

def ler_ficheiro():
    f = open('inscricoes.txt', 'r')
    lista = f.readlines()
    f.close()
    return lista

def mostrar_mensagem(nEstudantes, nDocentes, nExternos):
    messagebox.showinfo(title = 'Informação', message='{0} Estudantes {1} Docentes {2} Externos' .format(nEstudantes, nDocentes, nExternos))

def tree_dados():
    tree.delete(*tree.get_children())
    lista = ler_ficheiro()
    estudantes = 0
    docentes = 0
    externos = 0
    for linha in lista:
        campos = linha.split(';')
        tree.insert("", "end", values=(campos[0], campos[1]))
        if campos[1] == 'Estudante':
            estudantes += 1
        if campos[1] == 'Docente':
            docentes += 1
        if campos[1] == 'Externo':
            externos += 1
    mostrar_mensagem(estudantes, docentes, externos)

# THIRD ROW - IMAGE

def selecionaPerfil():
  """
  selecionar imagem a partir de FileDialog
  """
  global filename
  global image_id
  global ctn_image
  global nova_img

  filename = filedialog.askopenfilename(title = "Select file", initialdir= "./images", filetypes = (("png files","*.png"),("gif files", "*.gif"), ("all files","*")))

  nova_img = PhotoImage(file=filename)
  ctn_image.itemconfig(image_id, image=nova_img)

btn_selecionar_img = Button(window, text="Selecionar imagem", width=25, height=2, command=selecionaPerfil)
btn_selecionar_img.place(x=750, y=80)

ctn_image = Canvas(window, width=250, height=200, bd=2, relief="sunken")
ctn_image.place(x=750, y=150)

canva_img = PhotoImage(file='')
image_id = ctn_image.create_image(125,100, image=canva_img)

# BOTTOM OPTIONS

btn_ler_ficheiro = Button(window, text="Ler ficheiro", width=25, height=3, command=tree_dados)
btn_ler_ficheiro.place(x=20, y=520)

btn_add = Button(window, text="Adicionar", width=25, height=3, command=adicionar_inscricao)
btn_add.place(x=220, y=520)

btn_save = Button(window, text="Guardar", width=25, height=3)
btn_save.place(x=420, y=520)

label_n_inscritos = Label(text="N Inscrições")
label_n_inscritos.place(x=720, y=520)

n_inscritos_numero = IntVar()
entry_inscritos = Entry(window, width=10, show=n_inscritos_numero, state="disabled")
entry_inscritos.place(x=800, y=520)

# TODO: Mostrar total de inscritos na entry

window.mainloop()