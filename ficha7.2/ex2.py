import random

def iniciaMatriz(linhas, colunas):
    """
    cria a matriz
    """
    matriz = []
    for i in range(linhas):
        matriz.append([])
        for j in range(colunas):
            num = random.randint(10, 100)
            matriz[i].append(num)
    print("\n\t A matriz gerada foi: \n")
    for i in range(linhas):
        print("\t", matriz[i])
    print("--------------------------------------")
    return matriz
    
    
        

def matrizTransposta(matriz):
    """
    dá a matriz transposta da matriz gerada
    """
    print("\t Matriz transposta: \n")
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            print("\t", matriz[j][i], end = " ")
        print()
    print("--------------------------------------")
    return matriz


def maiorValor(matriz):
    """
    dá o maior valor da matriz gerada
    """
    maior = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] > maior:
                maior = matriz[i][j]
    print(" \t\n O maior valor da matriz é: ", maior)
    print("--------------------------------------")
    print()


print("\t MENU \n 1 – Inicializar matriz \n 2 - Matriz transposta \n 3 - Maior valor \n 0 - Sair")
resp = int(input("Escolha uma das opções: "))

while resp != 0:
    if resp == 1:
        numLinhas = int(input("Quantas linhas terá a matriz? "))
        numColunas = int(input("E quantas colunas? "))
        iniciaMatriz(numLinhas, numColunas)

    if resp == 2:
        numLinhas = int(input("Quantas linhas terá a matriz? "))
        numColunas = int(input("E quantas colunas? "))
        matriz = iniciaMatriz(numLinhas, numColunas)
        matrizTransposta(matriz)

    if resp == 3:
        numLinhas = int(input("Quantas linhas terá a matriz? "))
        numColunas = int(input("E quantas colunas? "))
        matriz = iniciaMatriz(numLinhas, numColunas)
        maiorValor(matriz)
        
    print("\t MENU \n 1 – Inicializar matriz \n 2 - Matriz transposta \n 3 - Maior valor \n 0 - Sair")
    resp = int(input("Escolha uma das opções: "))
