"""
programa que permita gerir uma fila de espera  com capacidade máxima para 20 lugares
Quando o programa se inicia, todos os lugares da fila devem estar livres. 
O seu programa deve conter um menu com as seguintes opções:
 MENU
1 – Tirar Ticket
2 - Atendimento
3 - Estado da fila de espera
0 - Sair"""

global fila
fila = []
for i in range(20):
    vaga = 0
    fila.append(vaga)
#print(fila)

def tirarTicket(fila):
    for i in range(len(fila)):
        if fila[i] == 0:
            fila[i] = 1
            return (i+1)
    return "Não é possível gerar mais ticekts"

""" i = 0
    while i != 1:
        for i in fila:
            if i == 0:
                fila[i] = 1
                i = 1
                pos = fila.index(i)
            elif i[20] == 1:
                print("Não é possível gerar mais ticekts")
            else:
                i=0
    return pos"""
    
def atendimento(fila):
    for i in range(len(fila)):
        if fila[i] == 0:
            fila[i] = 1
            return (i+1)

def filaEspera(fila):
    lugaresLivres = fila.count(0)
    lugaresOcupados = fila.count(1)
    print("\n\tLugares livres: {0} \n\tLugares ocupados: {1} \n" .format(lugaresLivres, lugaresOcupados))




print("\t MENU \n 1 – Tirar Ticket \n 2 - Atendimento \n 3 - Estado da fila de espera \n 0 - Sair")
resp = int(input("O que deseja fazer? "))

while resp != 0:
    if resp == 1:
        ticket = tirarTicket(fila)
        print("------------------")
        print(" \n \tO ticket tirado foi {0} \n" .format(ticket))
        print("------------------")
        resp = 0

    if resp == 2:
        att = atendimento(fila)
        print("------------------")
        print("\n \tA senha de espera é {0}\n" .format(att))
        print("------------------")
        resp = 0

    if resp == 3:
        print("------------------")
        filaEspera(fila)
        resp = 0
        print("------------------")
    print("\t MENU \n 1 – Tirar Ticket \n 2 - Atendimento \n 3 - Estado da fila de espera \n 0 - Sair")
    resp = int(input("O que deseja fazer? "))
