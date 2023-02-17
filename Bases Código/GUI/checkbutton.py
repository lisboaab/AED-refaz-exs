from tkinter import *
window = Tk()

checkCurto = IntVar()
checkUltra = IntVar()
check01 = Checkbutton(window, text="Trail Curto", variable = checkCurto, command=onChecked)  # uma variavel exclusiva pra cada botao
check02 = Checkbutton(window, text="Ultra Trail", variable = checkUltr, command=onCheckeda)
checkCurto.set(1)               # primeiro botao ativo por defeito
check01.place(x=60, y=20)
check02.place(x=170, y=20)