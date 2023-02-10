from tkinter import *

#--------FUNCOES-----------

def calculoPesoIdeal():
    if genSelected.get() == "Feminino":
        pesoIdeal = (h.get() - 100) - (h.get() -150)/2
        peso.delete("0.0", "end")
        peso.insert("1.0", pesoIdeal)
    elif genSelected.get() == "Masculino":
        pesoIdeal = (h.get() - 100) - (h.get() -150)/4
        peso.delete("0.0", "end")
        peso.insert("1.0", pesoIdeal)

#----------------------------    
class Application:
    def __init__(self, master=None):
        pass

# ------- GUI -----------

window = Tk()
window.geometry("800x500")
window.title("Ex 02 - Peso ideal")

screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()

appWidth = 1000
appHeight = 500

x = (screenWidth/2) - (appWidth/2)
y = (screenHeight/2) - (appHeight/2)
window.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
 
#----

lblAltura = Label(window, text="Altura (em cm): ")
lblAltura.place(x=50, y= 40)

h= IntVar()
altura = Entry(window, width=15, textvariable=h)
altura.place(x= 180, y=40)

frameGenero= LabelFrame(window, text=" Género: ", width=200, height=200)
frameGenero.place(x=50, y= 100)

genSelected = StringVar()
rdFem = Radiobutton(window, text="Feminino", value = "Feminino", variable= genSelected)
rdMasc = Radiobutton(window, text="Masculino", value = "Masculino", variable= genSelected)
rdFem.place(x=70, y= 140)
rdMasc.place(x=70, y= 220)

btnCalc = Button(window, text="Calcular peso ideal", height=10, width=20, command=calculoPesoIdeal)
btnCalc.place(x=270, y= 120)

framePeso= LabelFrame(window, width=200, height=200)
framePeso.place(x=450, y= 100)

lblPesoIdeal = Label(window, text="Peso ideal em KG: ")
lblPesoIdeal.place(x=500, y=150)

peso = Text(window, width=10, height=1)
peso.place(x=500, y=200)

window.mainloop()