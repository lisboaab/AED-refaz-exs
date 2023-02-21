guesTList = ['00-CC-00','01-CC-01','02-CC-02','03-CC-03','04-CC-04', '05-CC-05','06-CC-06','07-CC-07','08-CC-08','09-CC-09']
parklist = []

countEntrada = 0
matricula = ""

def parkManager(matricula,movimento):
    global countEntrada
    if movimento.upper() == "E":
        parklist.append(matricula)
        countEntrada += 1
        print(parklist)
    elif movimento.upper() == "S":
        parklist.remove(matricula)
        print("Saída concluída")
        print(parklist)
    print("Entradas: {0}" .format(countEntrada))


def parkvalidator(matricula,movimento):
    mov = ""
    if matricula not in guesTList:
        print("Matrícula não autorizada")
        mov = False
    elif movimento.upper() == "E":
        if matricula in guesTList and matricula not in parklist:
            mov = True
        else:
            mov = False
    elif movimento.upper() == "S":
        if matricula in parklist:
            mov = True
        else:
            mov = False
        if mov == False:
            print("Não é possível fazer esse movimento!")
    else:
        print("Movimento inserido inválido")

    if mov == True:
        parkManager(matricula,movimento)
            





while matricula != "00-00-00":
    matricula = input("Qual a sua matricula? ")
    movimento = input("Qual movimento deseja fazer? (Entrada-E; Saída-S) ")

    parkvalidator(matricula,movimento)