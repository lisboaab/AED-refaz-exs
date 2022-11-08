# recebe o nome completo e devolve o primeiro e o segundo nome

def shortName(name):
    primeiroEspaco = name.find(" ")
    if primeiroEspaco != -1:
        firstName = name[:primeiroEspaco]
    ultimoEspaco = name.rfind(" ")
    if ultimoEspaco != -1:
        secondName = name[ultimoEspaco:]
    print (firstName + secondName)

name = input("Insira o seu nome completo: ")
shortName(name)