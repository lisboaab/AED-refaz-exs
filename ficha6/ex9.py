"""
programa que permita ler o número de visitantes numa exposição (Domingo a Sábado).
Em seguida elabore uma função que permita listar o número de visitantes diário
por ordem decrescente. Indique ainda, no final, o número médio de visitantes por 
dia (com 2 casas decimais) e o dia que mais se aproximou do número médio de visitantes
"""
import math

diasSemana = ["Domingo", "Segunda" ,"Terça  ", "Quarta ", "Quinta ", "Sexta  ", "Sábado "]

def visitDecres(lista):
    listaOrdenada = lista.copy()
    listaOrdenada.sort(reverse=True)
    print("\n \t --------------------------- ")
    for i in range(len(lista)):
        posicao = lista.index(listaOrdenada[i])
        print("\t", diasSemana[posicao], "\t", listaOrdenada[i])
        lista[posicao]= -1

def diaMaisProximo(visitantes):
    media = sum(visitantes) / 7
    diferenca = math.inf  #math inf é um número infinito, meio que indeterminado que depois vai ser atribuido um valor a ele (linha 26)
    for i in range(len(diasSemana)):
        if abs(visitantes[i] - media) < diferenca:
            pos = i
            diferenca = abs(visitantes[i] - media) 
    return diasSemana[pos]

    """ visitMenosMedia = []
        for i in visitantes:
        newI = i - media
        visitMenosMedia.append(newI)
    menorNum = max(visitMenosMedia)
    pos = visitMenosMedia.index(menorNum)
    diaMaisProximo = diasSemana[pos]"""

visitantes = []

for i in diasSemana:
    visit = int(input("Quantos visitantes houveram {0}: " .format(i)))
    visitantes.append(visit)
    
i=0
print("\n --------------------------- ")
while i != 7:
    print(diasSemana[i] + ": ", visitantes[i])
    i += 1

media = float(sum(visitantes) / 7)



visitDecres(visitantes)
print ("Número médio de visitantes diários: {:.2f}" .format(media))
print ("O dia mais próximo do valor medio é: ", diaMaisProximo(visitantes))

