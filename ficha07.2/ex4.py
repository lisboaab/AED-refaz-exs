
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

def somaMatrizes(matriz1, matriz2):
    linhas = len(matriz1)
    colunas = len(matriz1[0])
    resultado = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(matriz1[i][j] + matriz2[i][j])
        resultado.append(linha)
    return resultado

def subMatrizes(matriz1, matriz2):
    linhas = len(matriz1)
    colunas = len(matriz1[0])
    resultado = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(matriz1[i][j] - matriz2[i][j])
        resultado.append(linha)
    return resultado


print("\t MENU \n 1 – Somar matrizes \n 2 - Subtrair matrizes \n  0 - Sair")
resp = int(input("Escolha uma das opções: "))

while resp != 0:
    if resp == 1:
        linhas = int(input("Quantas linhas terão as matrizes?"))
        colunas = int(input("E quantas colunas terão as matrizes?"))
        matriz1 = criamatriz(linhas, colunas)
        matriz2 = criamatriz(linhas, colunas)
        soma = somaMatrizes(matriz1, matriz2)
        print("------------------------------------- \n \t A soma das matrizes é: ")
        for linha in soma:
            print(linha)

    if resp == 2:
        linhas = int(input("Quantas linhas terão as matrizes?"))
        colunas = int(input("E quantas colunas terão as matrizes?"))
        matriz1 = criamatriz(linhas, colunas)
        matriz2 = criamatriz(linhas, colunas)
        subtracao = subMatrizes(matriz1, matriz2)
        print("------------------------------------- \n \t A subtração das matrizes é: ")
        for linha in subtracao:
            print(linha)

    print("--------------------------------------------")
    print("\t MENU \n 1 – Somar matrizes \n 2 - Subtrair matrizes \n  0 - Sair")
    resp = int(input("Escolha uma das opções: "))