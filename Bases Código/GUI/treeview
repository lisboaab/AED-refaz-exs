from tkinter import *
from tkinter import ttk

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


# BASE DA TREEVIEW -------------------------------------
tree = ttk.Treeview(window, selectmode= "browse", columns = ("Col1", "Col2", "Col3"), show = "headings")
tree.place(x= 00, y= 00)
tree.column("coluna", width= 00 ; anchor = e) # c - centro; e -  direita; w - esquerda
tree.heading("Nome", text ="Nome")

tree.insert("", "end", values = (campos[0], campos[1], [2]))





# PEGA DE UMA TREEVIEW E COLOCA NA LISTBOX ----------------------------------------------
def adcFavorito():
    pos = tree.selection()

    # Iterar sobre os índices selecionados
    for index in pos:
        # Obter os valores do item selecionado na treeview
        values = tree.item(index)['values'][0]
        
        # Adicionar os valores na listbox
        listBox.insert('end', values)
        
        

 


window.mainloop()