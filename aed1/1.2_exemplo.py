def imprime_palavras(texto1):
    pos = texto1.find(" ")
    while pos != -1:
        cont_pal = 0
        pal = texto1[:pos] # 
        print(pal)
        cont_pal += 1
        pos = texto1.find(" ", pos+1)

texto = input("Texto: ") + " "
cont = imprime_palavras(texto)

print("O texto contém", cont_pal, "palavras")


# erros: 
# 1: variável "cont_pal" não foi definida antes
# 2: linha 5 o que vai definir uma palavra é [:pos]
# 3: última linha não printa a quantidade de palavras presentes no texto inserido