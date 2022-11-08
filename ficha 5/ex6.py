# funç˜˜˜ào que dá o nome completo mas com siglas

def standardName(name):
    primeiroEspaco = name.find(" ")
    firstName = name[:primeiroEspaco]

    ultimoEspaco = name.rfind(" ")
    lastName = name[ultimoEspaco:]

    for i in range(primeiroEspaco, ultimoEspaco):
        if name[i] == " ":
            middleName = " " + name[i+1] + "."
    completeName = firstName + middleName + lastName

    return completeName


name = input("Insira o seu nome completo: ")
print (standardName(name))