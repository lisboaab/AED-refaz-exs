# programa que permita gerir a ocupação de um pequeno parque de estacionamento
# status: opcao 1(def entrada veiculo): parte "o parque está cheio não funciona"

import os

def criaParque(lugares, filas):
    ''' cria o parque com todos os lugares vazios '''
    lista = []
    for i in range(filas):
        lista.append([])
        for j in range(lugares):
            lista[i].append(0)
    return lista

def entradaVeiculo():
    '''  Deve indicar na consola a posição do lugar a ocupar. Se todos os lugares 
    estiverem ocupados deverá surgir a mensagem de “Parque completo" '''
    for i in range(filas):
        for j in range(lugares):
            if parque [i][j] == 0:
                parque [i][j] = 1
                print("O lugar opcupado foi na fila {0} lugar {1}" .format(i+1, j+1))
                return parque
    #print ("\t O parque está cheio!")
    #return parque
    

def saidaVeiculo():
    ''' O utilizador deve indicar a posição, na fila de estacionamento, do
    carro que pretende sair (fila e lugar). Esse lugar deve passar ao estado 
    de livre.
    '''
    try:
        lugarSaida = int(input("De qual lugar seu vaículo vai sair? "))
        filaSaida = int(input("E de qual fila? "))
        if lugarSaida > lugares:
            raise ValueError()
        if filaSaida > filas:
            raise ValueError()
    except:
        print("Valores indicados inválidos")
    else:
        if parque[filaSaida][lugarSaida] == 0:
            print("\n \t O lugar não está ocupado.\n")
        else:
            parque[filaSaida][lugarSaida] = 0
            print("\n \t O lugar foi desocupado!\n")
    return parque

def estadoParque():
    ''' esta opção deve indicar, na consola, o número de lugares
    ocupados e o número de lugares livres, no parque. '''
    lugaresLivres = 0
    lugaresOcupados = 0
    for i in range(filas):
        for j in range(lugares):
            if (parque[i][j] == 0):
                lugaresLivres += 1
            else:
                lugaresOcupados += 1
    print("\n \t O estado do parque é: ")
    print("\t \t Lugares livres: {0}" .format(lugaresLivres))
    print("\t \t Lugares ocupados: {0} \n" .format(lugaresOcupados))


# menu e opções:
resp = " "
while resp != 0:
    # os.system("cls")
    print("\t \n MENU")
    print("1 - Entrada de veículo")
    print("2 - Saída de veículo")
    print("3 - Estado do parque")
    print("0 - Sair")

    filas = 3
    lugares = 5
    parque = criaParque(lugares, filas)

    resp = input("Insira uma opção: ")

    if resp == "1":
        parque = entradaVeiculo()
    elif resp == "2":
        parque = saidaVeiculo()
    elif resp == "3":
        estadoParque()
    elif resp == "0":
        break
    else:
        print("Dado inserido inválido. Tente Novamente.")
