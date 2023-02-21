def imprime_palavras(texto1):
    #...........
    pos = texto1.find(" ")   
    cont_pal = 0        # cont_pal não é definido antes
    while pos != -1:
        pal = texto1[cont_pal:pos]
        print(pal)
        cont_pal+=1
        pos = texto1.find(" ", pos+1)

texto = input("Texto: ") + " "
cont = imprime_palavras(texto)

# print teria q ser cont_pal pra dizer a quantidade de palavras
# funcao nao printa como o desejado