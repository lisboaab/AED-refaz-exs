from tkinter import *
from tkinter import messagebox

#--------FUNCOES-----------
def criaLista():
    """
    Cria a lista de tarefas"""
    file = open(".\\ficha11\\ex03-ToDoList\\tarefas.txt", "r", encoding="utf-8")
    lista = file.readlines()
    file.close()
    return lista

def adicionar():
    """
    Adiciona a tarefa escrita na lista"""
    append = txtTarefa.get("1.0", "end")
    file = open(".\\ficha11\\ex03-ToDoList\\tarefas.txt", "a", encoding="utf-8")
    file.write(append)
    file.close()
    tarefas.insert("end", append)

def remover():
    """Apaga a tarefa selecionada da listbox"""
    pos = tarefas.curselection()   # obtem o índice da linha ativa 
                                   # OU: lboxTarefas.focus()
    if len(pos) >0:
    # Remove o item selecionado da Listbox
        tarefas.delete(tarefas.curselection())   # indice do item selecionado
        with open(".\\ficha11\\ex03-ToDoList\\tarefas.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
        with open(".\\ficha11\\ex03-ToDoList\\tarefas.txt", "w", encoding="utf-8") as f:
            for i, line in enumerate(lines):
                if i != pos[0]:
                    f.write(line)
    else:
        messagebox.showerror("info", "Não existem dados selecionados")        

def clear():
    """
    Limpa a listbox"""
    tarefas.delete(0, "end")

def upload():
    """
    Cria a lista de tarefas"""
    file = open(".\\ficha11\\ex03-ToDoList\\tarefas.txt", "r", encoding="utf-8")
    lista = file.readlines()
    file.close()
    tarefas.delete(0, "end")
    for linha in lista:
        tarefas.insert("end", linha)

def download():
    """
    Guardar lista de tarefas em file
    """
    fileTarefas = open(".\\ficha11\\ex03-ToDoList\\tarefas.txt", "w", encoding="utf-8")
    cont = tarefas.size()                   # conta nº d etarefas na ListBox
    for i in range(cont):                       # Iterar tarefas
           atividade = tarefas.get(i)       # Obter cada uma das tarefas da ListBox 
           if atividade.find("\n") == -1:
               atividade = atividade + "\n"
           fileTarefas.write(atividade)         # Guarda em ficheiro
    fileTarefas.close() 

def ordenar():
    """Ordena lista de tarefas em ordem alfabetica"""
    file = open(".\\ficha11\\ex03-ToDoList\\tarefas.txt", "r", encoding="utf-8")
    lista = file.readlines()
    file.close()
    lista.sort()
    tarefas.delete(0, "end")
    for linha in lista:
        tarefas.insert("end", linha)

#----------------------------    
class Application:
    def __init__(self, master=None):
        pass

# ------- GUI -----------

window = Tk()
window.geometry("800x500")
window.title("Ex 03 - To do list")

screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()

appWidth = 1000
appHeight = 500

x = (screenWidth/2) - (appWidth/2)
y = (screenHeight/2) - (appHeight/2)
window.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
 
#----

frame1 = LabelFrame(window, width=300, height=300)
frame1.place(x=20, y=30)

listaTarefas = criaLista()
tarefas = Listbox(window, selectmode="single", width=45, height=15)
for i in listaTarefas:
    tarefas.insert("end", i)
tarefas.place(x=30, y=40)


frame2 = LabelFrame(window, width=400, height=100)
frame2.place(x=400, y=30)
lblTarefa = Label(window, text="Tarefa: ")
lblTarefa.place(x=420, y=60)
txtTarefa = Text(window, width=30, height=1)
txtTarefa.place(x=480, y=60)


btnAdd = Button(window, text="Adicionar", width=15, height=3, command=adicionar)
btnAdd.place(x=420, y=200)

btnRemov = Button(window, text="Remover", width=15, height=3, command=remover)
btnRemov.place(x=550, y=200)

btnClear = Button(window, text="Clear", width=15, height=3, command=clear)
btnClear.place(x=680, y=200)

btnUpload = Button(window, text="Upload", width=15, height=3, command=upload)
btnUpload.place(x=420, y=270)

btnDownload = Button(window, text="Download", width=15, height=3, command=download)
btnDownload.place(x=550, y=270)

btnOrdenar = Button(window, text="Ordenar", width=15, height=3, command=ordenar)
btnOrdenar.place(x=680, y=270)

window.mainloop()