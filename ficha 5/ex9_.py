def countWord(texto, palavra):
    ocorrencias = texto.count(palavra)
    posicao = texto.find(palavra)
    return ("ocorre {0} vezes" .format(ocorrencias))
    return ("Está na posição {0}" .format(posicao))

texto = input("Insira um texto: ")
palavra = input("Qual palavra deseja pesquisar? ")
print (countWord(texto, palavra))


# nao soube colocar p funcionar o find
# e nao entendi oq o prof fez:
# ant=0           
#    positions=""     # variável de saida com as diversas posições no texto
#   for i in range(num):
#        pos = text.find(txtFind, ant) # pesquisa (find) no texto a partir da posição ant
#        if pos != -1:
#            positions+= " " + str(pos+1)   
#            ant = pos + 1
#        else:
#            break