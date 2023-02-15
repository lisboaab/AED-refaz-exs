# status = matriz transposta não funciona
#               (quando resolvi deu: na linha 39 dá "list index out of range" mas funciona)

import random

def inicializaMatriz(linhas, colunas):
    ''' gera uma matriz aleatória com numeros entre 10 e 100, com os parametros definidos pelo utilizador '''
    matriz = []
    for i in range(linhas):
        matriz.append([])
        for j in range(colunas):
            num = random.randint(10,100)
            matriz[i].append(num)
    print("\nA matriz gerada é: ")
    for linha in matriz:
        print(linha)


def matrizTransposta():
    """ recebe uma matriz e imprime a transposta """
    
    # recebe matriz original
    linhas = int(input("Quantas linhas sua matriz terá? "))
    colunas = int(input("E quantas colunas? "))
    matriz = []
    pos = 0
    for i in range(linhas):
        matriz.append([])
        for j in range(colunas):
            numero = int(input("Insira um número para a posição {0} da matriz: ".format(pos)))
            pos+=1
            matriz[i].append(numero)
    print("\nA matriz que geraste é: ")
    for linha in matriz:       #printa a matriz gerada pelo usuário
        print(linha)
    
    
    # cria a matriz transposta
    print("\nMatriz Transposta:")
    for i in range(len(matriz)):
        for j in range (len(matriz)):                       
            print(matriz[j][i], end = " ")
        print()
    

def maiorValor():
    # recebe matriz original
    linhas = int(input("Quantas linhas sua matriz terá? "))
    colunas = int(input("E quantas colunas? "))
    matriz = []
    pos = 0
    for i in range(linhas):
        matriz.append([])
        for j in range(colunas):
            numero = int(input("Insira um número para a posição {0} da matriz: ".format(pos)))
            pos+=1
            matriz[i].append(numero)
    print("\nA matriz que geraste é: ")
    for linha in matriz:       #printa a matriz gerada pelo usuário
        print(linha)

    matrizMaxima = []           # cria lista pra adicionar o maximo de cada sub-lista
    for i in range(len(matriz)):
        matrizMaxima.append(max(matriz[i]))        #faz o append dos itens max de casa lista

    print("\n O valor máximo da sua matriz é {0} \n" .format(max(matrizMaxima)))  
   



# menu e escolha de opções
opcao = " "
while opcao != 0:
    print("\t MENU")
    print("1 - Inicializar matriz")
    print("2 - Matriz transposta")
    print("3 - Maior valor")
    print("0 - Sair")
    opcao = input("Escolha uma das opções: ")
    if opcao == "1":
        linhas = int(input("Quantas linhas sua matriz terá? "))
        colunas = int(input("E quantas colunas? "))
        matriz = inicializaMatriz(linhas, colunas)
        opcao = 0
    elif opcao == "2":
        matrizTransposta()
        opcao = 0
    elif opcao == "3":
        maiorValor()
        opcao = 0
    elif opcao == "0":
        break
    else:
        print("\n \t Valor inserido inválido. Tente novamente. \n")
