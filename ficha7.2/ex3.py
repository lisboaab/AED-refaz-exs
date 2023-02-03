estacionamento = []
linhas = 3
colunas = 5
for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(0)         # inicializa as vagas como livres (0)
    estacionamento.append(linha)

def entrada(estacionamento):
    for i in range(linhas):
        for j in range(colunas):
            if estacionamento[i][j] == 0:
                estacionamento[i][j] = 1
                return (i+1, j+1)
    return "Parque completo"

def saidaCarro(filaSaida, colunaSaida):
    saida = filaSaida - 1
    saida1 = colunaSaida - 1
    estacionamento[saida][saida1] = 0
    print("A vaga foi liberada!")


def estadoParque(estacionamento):
    lugaresLivres = 0
    lugaresOcupados = 0
    for i in range(linhas):
        for j in range(colunas):
            if estacionamento[i][j] == 0:
                lugaresLivres += 1
            else:
                lugaresOcupados += 1
    print("\n\tLugares livres: {0} \n\tLugares ocupados: {1} \n" .format(lugaresLivres, lugaresOcupados))


print("\t MENU \n 1 – Entrada de veículo \n 2 - Saída de carro \n 3 - Estado do Parque \n 0 - Sair")
resp = int(input("Escolha uma das opções: "))

while resp != 0:
    if resp == 1:
        vaga = entrada(estacionamento)
        print("Ocupe o lugar fila: {0} colunha: {1}" .format(vaga[0], vaga[1]))

    if resp == 2:
        filaSaida= int(input("De qual fila quer sair? "))
        colunaSaida= int(input("E coluna? "))
        saidaCarro(filaSaida, colunaSaida)

    if resp == 3:
       estadoParque(estacionamento)
        
    print("\t MENU \n 1 – Entrada de veículo \n 2 - Saída de carro \n 3 - Estado do Parque \n 0 - Sair")
    resp = int(input("Escolha uma das opções: "))