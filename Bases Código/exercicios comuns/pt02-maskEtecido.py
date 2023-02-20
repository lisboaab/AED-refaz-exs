lmask = []
ltecido = []

def topMask(lmask):
    maior = 0
    maior2 = 0
    pos1 = 0
    pos2 = 0
    for numero in lmask:
        if numero > maior:
            maior2 = maior
            maior = numero
        elif numero > maior2:
            maior2 = numero
    
    for i in range(len(lmask)):
        if lmask[i] == maior:
            pos1 = (i+1)
        elif lmask[i] == maior2:
            pos2 = (i+1)
    print("Os postos que mais produziram máscaras foram {0} e {1}" .format(pos1, pos2))


def moreMaterial(lmask, ltecido):
    medias = []
    for i in range(len(lmask)):
        numM = lmask[i]
        tec = ltecido[i]
        valor = tec/numM
        medias.append(valor)
    pos = medias.index(max(medias)) + 1
    print("O posto que mais gastou tecido foi {0}" .format(pos))




try:
    for i in range(3):
        numMasc = int(input(f"Quantas máscaras foram produzidas no posto {i+1}? "))
        tecido = int(input(f"Quantos cm de tecido foram gastos no posto {i+1}? "))
        print("\n")
        if tecido < 0 or tecido > 15:
            raise ValueError()
        else:
            ltecido.append(tecido)
            lmask.append(numMasc)

except ValueError:
    print("Dado inválido")

topMask(lmask)
moreMaterial(lmask, ltecido)
    

