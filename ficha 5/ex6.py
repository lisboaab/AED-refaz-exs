# funç˜˜˜ào que dá o nome completo mas com siglas

def standardName(name):
    primeiroEspaco = name.find(" ")
    firstName = name[:primeiroEspaco]
    ultimoEspaco = name.rfind(" ")
    lastName = name[ultimoEspaco:]
    middleName = name[" ":" "]
    middleName1 = middleName[0] + "." 
    return firstName + middleName + lastName

name = input("Insira o seu nome completo: ")
standardName(name)