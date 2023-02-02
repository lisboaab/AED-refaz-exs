"""Dado uma lista de N elementos (N deve ser pedido ao utilizador), crie uma 
função que ordene a lista e que permita gerar uma outra lista sem valores duplicados."""

def ordenaLista(lista):
    listaSemRepeticao = []
    for i in range(len(lista)):
        if listaSemRepeticao.count(lista[i]) == 0:
            listaSemRepeticao.append(lista[i])
    listaOrdenada = sorted(listaSemRepeticao)
    return listaOrdenada

listaNums = []
n = int(input("Quantos elementos teve ter sua lista? "))
for i in range(n):
    num = int(input("Insira um número: "))
    listaNums.append(num)

novaLista = ordenaLista(listaNums)
print("A nova lista é: ", novaLista)