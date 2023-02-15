""" 
Elabore um programa que leia uma lista de 10 números inteiros.
Em seguida, dado um determinado valor de pesquisa, invoque a função searchNumber(lista, pesquisa)
que deve devolver as posições em que encontra o valor de pesquisa, na lista.
Caso o valor de pesquisa não exista na lista, deve surgir uma mensagem adequada.
"""

def searchNumber(lista, pesquisa):
    posicoes = []
    for pos, i in enumerate(lista):
        if i == pesquisa:
            posicoes.append(pos)
    if not posicoes:   # checa se a lista está vazia
        return -1
    return posicoes


listaNumeros = []
for i in range(10):
    try:
        num = int(input("Insira um número: "))
    except ValueError:
        print("O valor inserido não é um interio, tente novamente!")
    except:
        print("Dado inválido. Tente novamente!")
    else: 
        listaNumeros.append(num)
pesquisa = int(input("Qual número deseja pesquisar? "))
posicoes = (searchNumber(listaNumeros, pesquisa))

if posicoes == -1:
    print("O número {0} não existe na lista" .format(pesquisa))
else:
    print("O número {0} encontra-se nas posições {1}" .format(pesquisa, posicoes))