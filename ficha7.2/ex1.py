"""
Dada uma matriz 3x3 de inteiros, cujos valores são indicados pelo utilizador, 
elabore uma função invert que receba a matriz lida e imprima, assim como à sua transposta.
"""



def criamatriz(linhas, colunas):
    """
    cria a matriz
    """
    matriz = []
    for i in range(linhas):
        matriz.append([])
        for j in range(colunas):
            num = int(input("Qual número deseja adicionar na linha {0} e coluna {1}? " .format(i+1, j+1)))
            matriz[i].append(num)
    return matriz

def transposta(matriz):
    """
    dá a matriz transposta da matriz gerada
    """
    print("\n \t Matriz Original:")
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            print("\t", matriz[i][j], end = " ")
        print()
    print("\n -----------------------------------------------")

    print("\n \t Matriz Transposta: ")
    
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            print("\t", matriz[j][i], end = " ")
        print()


matriz = criamatriz(2,2)
transposta(matriz)
