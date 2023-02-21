def printCharline (texto, caracteres):
    try:
        if caracteres < 1 or caracteres >12:
            raise ValueError()
        while caracteres < len(texto):
            print(texto[:caracteres])
            texto = texto[caracteres:]
        print(texto)
        
    except ValueError:
        print("Valor inserido invalido")


texto = input("Insira um texto: ")
caracteres = int(input("Quantos caracteres quer por linha? "))
printCharline(texto, caracteres)