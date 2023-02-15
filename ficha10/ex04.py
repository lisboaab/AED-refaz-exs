from tkinter import *

# -----------FUNCOES--------
def sair():
    """
    opção de sair, terminar
    """
    # window.quit()     # fecha o container window
    window.destroy()    # fecha e remove da memoria


def calcIMC():
    massa = int(kg.get())
    heigth = float(altura.get())
    imc =  massa/(heigth*heigth)
    txtResultado.delete("0.0","end")
    txtResultado.insert("end", imc)


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


frame1 = LabelFrame(window, width=300, height=100)
frame1.place(x=30, y=20)

lblPeso = Label(window, text="Peso (em kg): ")
lblPeso.place(x=50, y= 40)

peso= IntVar()
kg = Entry(window, width=15, textvariable=peso)
kg.place(x= 180, y=40)


lblAltura = Label(window, text="Altura (em M): ")
lblAltura.place(x=50, y= 80)

h= IntVar()
altura = Entry(window, width=15, textvariable=h)
altura.place(x= 180, y=80)

frame2 = LabelFrame(window, width=300, height=100)
frame2.place(x=30, y=200)
lblIMC = Label(window, text="Indice de Massa Corporal\nResultado: ")
lblIMC.place(x=110, y= 210)
result = StringVar
txtResultado = Text(window, height=1, width=8) 
txtResultado.place(x=160, y=250)

btnCalcIMC = Button(window, text="Calcular IMC", width=10, height=5, command=calcIMC)
btnCalcIMC.place(x=370, y= 100)
btnSair = Button(window, text="Sair", width=10, height=5,command=sair)
btnSair.place(x=370, y= 200)


ctn_canvas = Canvas(window, width = 270, height = 180, bd = 2, relief = "sunken")
ctn_canvas.place(x=500, y=40)

img = PhotoImage(file = ".\\ficha11\\ex04\\IMC.gif")
ctn_canvas.create_image(135,90, image = img)

window.mainloop()