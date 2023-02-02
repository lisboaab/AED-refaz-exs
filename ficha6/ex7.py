"""
O Instituto de metereologia pretende registar o valor total de pluviosidade ocorrida em
cada mês, ao longo de um ano (de janeiro a dezembro). Implemente a função pluviosidade que 
receba a lista com a pluviosidade de cada mês, e imprima esses mesmos dados (lista de 
pluviosidade), mas ordenados por ordem decrescente de pluviosidade. Upgrade versão 2.0: 
imprimir também os nomes dos respetivos meses, como na imagem!
"""

meses = ["Janeiro   ", "Fevereiro", "Março     ", "Abril     ", "Maio     ", "Junho    ", "Julho    ", "Agosto   ", "Setembro   ", "Outubro   ", "Novembro", "Dezembro"]

def pluviosidade(lista):
    listaOrdenada = lista.copy()
    listaOrdenada.sort(reverse=True)
    for i in range(len(lista)):
        posicao = lista.index(listaOrdenada[i])
        print("\t", meses[posicao], "\t", listaOrdenada[i])
        lista[posicao]= -1


pluviosidadeMes = []
for mes in meses:
    pluv = int(input("Pluviosidade do mês de {0}: ".format(mes)))
    pluviosidadeMes.append(pluv)
print("\n Pluviosidade:")

pluviosidade(pluviosidadeMes)


"""
    for mes, pluv in enumerate(pluviosidadeMes):
    
    print("--------------------------------------")
    print(meses[mes], "\t Pluviosidade:", pluv)
    """
