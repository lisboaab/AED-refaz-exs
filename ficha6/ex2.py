import random

def generateNumbers (min, max, qty):
    numeros = []
    i = 0
    while i != qty:
        num = random.randint(min,max)
        if num not in numeros:
            numeros.append(num)
    return numeros

def euroMilhoes():
    resp = "S"
    while resp.upper() != "N":
        chaveEuromilhoes = generateNumbers(1,50,5)
        chaveEstrelas = generateNumbers(1,12,2)

        print("Chave do Euromilhoes: {0} \n Estrelas: {1}" .format(chaveEuromilhoes, chaveEstrelas))
        resp = input("Deseja gerar novas chaves? (S/N) ")

euroMilhoes()