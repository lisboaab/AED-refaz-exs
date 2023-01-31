# função aboveAverage que receba uma lista com 10 números inteiros 
# (número inseridos pelo utilizador) e que devolva quantos desses números 
# estão acima da média.

def aboveAverage():
    numeros = []
    for i in range(10):
        num = int(input("Insira o número {0}: " .format(i + 1)))
        numeros.append(num)
    soma = sum(numeros)
    media = float(soma/10)
    acimaMedia = []
    for num in numeros:
        if num > media:
            acimaMedia.append(num)
    # print("A media e: {0}" .format(media))
    # print(acimaMedia)
    print("Existem {0} números acima da média" .format(len(acimaMedia)))

aboveAverage()
    