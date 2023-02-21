# erros do ex como comentario aqui, ao ser comparado com o ex do prof
def pares(numeros):   # def nao tem descricao
    cont = 0
    for i in range(len(numeros)):
        if numeros[i] % 2 == 0:    # falta um = aqui
            cont += 1
        return cont
        

numeros = []
n = int(input("Quantos numeros quer ler?"))
for i in range(n):
    num = int(input("Numero:"))
    numeros.append(num)

                                                                # chama o resultado fora da linha do print
print("A lista .... {0} nums pares" .format(pares(numeros)))