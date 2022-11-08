# recebe o nome completo e devolve o primeiro e o segundo nome

def shortName(name):
    primeiroEspaco = name.find(" ")
    firstName = name[:primeiroEspaco]
    ultimoEspaco = name.rfind(" ")
    secondName = name[ultimoEspaco:]
    return firstName + secondName

name = input("Insira o seu nome completo: ")
shortName(name)