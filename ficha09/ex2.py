def consultaData(data):
    file = open("ficha9/temperatura.txt", "r", encoding="utf-8")
    lista = file.readlines()
    file.close()
    print("\t Data \t \t Hora \t     Temperatura")
    print("--------------------------------------------------------------------")
    for linha in lista:
        div = linha.split(";")
        date = div[0]
        hora = div[1]
        temperatura = div[2]
        if data == date:
            print("\t" + date + "\t" + hora + "\t" + temperatura)

def estatistica():
    file = open("ficha9/temperatura.txt", "r", encoding="utf-8")
    lista = file.readlines()
    file.close()

    temperaturas = []
    for linha in lista:
        div = linha.split(";")
        date = div[0]
        hora = div[1]
        temperatura = div[2]
        temp = int(temperatura)
        temperaturas.append(temp)
    
    soma = sum(temperaturas)
    media = soma / len(temperaturas)
    maximo = max(temperaturas)
    minimo = float(min(temperaturas))
    print("----------------------------------------------")
    print("A maior temperatura registrada foi", maximo)
    print("A menor temperatura registrada foi", minimo)
    print("A temperatura media registrada foi", media)
    print()


print("\t MENU \n 1 – Consultar por data \n 2 - Consulta Estatística \n 0 - Sair")
resp = int(input("Escolha uma das opções: "))

while resp != 0:
    if resp == 1:
        data = input("Qual data deseja pesquisar? Formato: ano-mês-dia  ")
        print(consultaData(data))

    if resp == 2:
        estatistica()

    print("--------------------------------------------")
    print("\t MENU \n 1 – Consultar por data \n 2 - Consulta Estatística \n 0 - Sair")
    resp = int(input("Escolha uma das opções: "))