# recebe os numeros e cria as matrizes orginal e transposta desses numeros
# status: done!


def criaLista(numLin, numCol):
    lista = []
    for i in range(numLin):
        lista.append([])
        for j in range(numCol):
            numero = int(input("Insira um numero para a linha {0} e coluna {1}: " .format(i+1, j+1)))
            lista[i].append(numero)         # em cada linha, acrescenta uma coluna à lista  
    return lista     
   
 

def invert(lista):
    print("\nMatriz Original: ") 
    for i in range(len(lista)):             
        for j in range(len(lista)):           
            print(lista[i][j], end = " ")
        print()
    
    print("\nMatriz Transposta: ")
    for i in range(len(lista)):
        for j in range(len(lista)):
            print(lista[j][i], end = " ")
        print()

lista = criaLista(3, 3)
invert(lista)

