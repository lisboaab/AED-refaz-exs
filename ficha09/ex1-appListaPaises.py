def inserirPaises():
    pais = input("País: ")
    continente = input("Continente: ")
    
    file = open("ficha09/paises.txt", "r", encoding="utf-8")
    lista = file.readlines()
    file.close()
    
    pais_ja_existe = False
    for linha in lista:
        if linha == (pais + ";" + continente + ";\n"):
            pais_ja_existe = True
            break
    
    if pais_ja_existe:
        print("\n \t País já existe na lista")
    else:
        file = open("ficha09/paises.txt", "a", encoding="utf-8")
        file.write("\n" + pais + ";" + continente + ";")
        file.close()
        print("\n \t País adicionado na lista")


def printPaises():
    file = open("ficha09/paises.txt", "r", encoding="utf-8")
    lista = file.readlines()
    file.close()
    print("País         Continente  \n------------------------------")
    for linha in lista:
        div = linha.split(";")
        pais = div[0]
        continente = div[1]
        print(pais + "  |  " + continente)
        print()

def consultaContinente(continente):
    file = open("ficha09/paises.txt", "r", encoding="utf-8")
    lista = file.readlines()
    file.close()    
    
    print("País    Continente  \n------------------------------")
    for linha in lista:
        divisao = linha.split(";")
        pais = divisao[0]
        cont = divisao[1]
        
        if continente == cont:
            print(divisao[0] + " | " + divisao[1])
    if continente not in cont:
        print("\n \t Continente não encontrado na lista")
        print()
               


def contarPaises():
    file = open("ficha09/paises.txt", "r", encoding="utf-8")
    lista = file.readlines()
    file.close()    
    
    countEuropa = 0
    countAsia = 0
    countOceania = 0
    countAmerica = 0
    countAfrica = 0
    countOutro = 0
    
    for linha in lista:
        div = linha.split(";")
        if div[1] == "Europa":
            countEuropa += 1
        elif div[1] == "Asia":
            countAsia += 1
        elif div[1] == "Oceania":
            countOceania += 1
        elif div[1] == "America":
            countAmerica += 1
        elif div[1] == "Africa":
            countAfrica += 1
        else:
            countOutro += 1
    print()
    print("Paises Europa: ", countEuropa, "\nPaises Asia: ", countAsia, "\nPaises Oceania: ", countOceania, "\nPaises America: ", countAmerica, "\nOutros: ", countOutro)


print("\t MENU \n 1 – Inserir Paises \n 2 - Consulta Paises \n 3 - Consulta por continente \n 4 - Consulta nº paises \n 0 - Sair")
resp = int(input("Escolha uma das opções: "))

while resp != 0:
    if resp == 1:
       inserirPaises()

    if resp == 2:
        printPaises()

    if resp == 3:
        continente = input("Qual continente deseja pesquisar? ")
        consultaContinente(continente)

    if resp == 4:
        contarPaises()

    
    print("\n \t MENU \n 1 – Inserir Paises \n 2 - Consulta Paises \n 3 - Consulta por continente \n 4 - Consulta nº paises \n 0 - Sair")
    resp = int(input("Escolha uma das opções: "))