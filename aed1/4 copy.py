# Considere uma fábrica que dispõe de uma linha de produção de máscaras, constituída por 6 postos de trabalho.
# Implemente um programa que leia, para cada posto de trabalho, a produção (nº de máscaras produzidas) e o tecido
# gasto (em cm).
# Com base nestes dados, implemente as seguintes funções:
# • Função que devolva os dois postos de trabalho que produziram maior número de máscaras
# • Função que devolva qual o posto de trabalho que gastou mais tecido

def maiorNumMascaras (masc1, masc2, masc3, masc4, masc5, masc6, mascaras):
    mascaras = []   
    # -------------------- coloca os dados na lista mascaras:
    mascaras.append(masc1)
    mascaras.append(masc2)
    mascaras.append(masc3)
    mascaras.append(masc4)
    mascaras.append(masc5)
    mascaras.append(masc6)
    # -------------------- diz qual posto mais produziu mascaras:
    mascaras.sort()
    if max(mascaras) == masc1:
        print("O posto que mais produziu mascaras foi o Posto 1")
    elif max(mascaras) == masc2:
        print("O posto que mais produziu mascaras foi o Posto 2")
    elif max(mascaras) == masc3:
        print("O posto que mais produziu mascaras foi o Posto 3")
    elif max(mascaras) == masc4:
        print("O posto que mais produziu mascaras foi o Posto 4")
    elif max(mascaras) == masc5:
        print("O posto que mais produziu mascaras foi o Posto 5")
    else:
        print("O posto que mais produziu mascaras foi o Posto 6")
      # -------------------- diz qual segundo posto mais produziu mascaras:
    del mascaras[5]
    if max(mascaras) == masc1:
        print("O segundo posto que mais produziu mascaras foi o Posto 1")
    elif max(mascaras) == masc2:
        print("O segundo posto que mais produziu mascaras foi o Posto 2")
    elif max(mascaras) == masc3:
        print("O segundo posto que mais produziu mascaras foi o Posto 3")
    elif max(mascaras) == masc4:
        print("O segundo posto que mais produziu mascaras foi o Posto 4")
    elif max(mascaras) == masc5:
        print("O segundo posto que mais produziu mascaras foi o Posto 5")
    else:
        print("O segundo posto que mais produziu mascaras foi o Posto 6")


def maisTecido (p1, p2, p3, p4, p5, p6, cmTecido):
    cmTecido = []   
    cmTecido.append(p1)
    cmTecido.append(p2)
    cmTecido.append(p3)
    cmTecido.append(p4)
    cmTecido.append(p5)
    cmTecido.append(p6)
    # -------------------- diz qual posto mais produziu mascaras:
    cmTecido.sort()
    if max(cmTecido) == p1:
        print("O posto que gastou mais tecido foi o Posto 1")
    elif max(cmTecido) == p2:
        print("O posto que gastou mais tecido foi o Posto 2")
    elif max(cmTecido) == p3:
        print("O posto que gastou mais tecido foi o Posto 3")
    elif max(cmTecido) == p4:
        print("O posto que gastou mais tecido foi o Posto 4")
    elif max(cmTecido) == p5:
        print("O posto que gatou mais tecido foi o Posto 5")
    else:
        print("O posto que gastou mais tecido foi o Posto 6")


mascaras = []
cmTecido = []
pronto = 0

while pronto != 1:
    try:
        masc1 = int(input("Quantas máscaras o posto 1 produziu? "))
        p1 = int(input("Quantos cm de tecido o posto 1 gastou? "))
        masc2 = int(input("Quantas máscaras o posto 2 produziu? "))   
        p2 = int(input("Quantos cm de tecido o posto 2 gastou? "))
        masc3 = int(input("Quantas máscaras o posto 3 produziu? "))  
        p3 = int(input("Quantos cm de tecido o posto 3 gastou? "))
        masc4 = int(input("Quantas máscaras o posto 4 produziu? ")) 
        p4 = int(input("Quantos cm de tecido o posto 4 gastou? "))
        masc5 = int(input("Quantas máscaras o posto 5 produziu? "))   
        p5 = int(input("Quantos cm de tecido o posto 5 gastou? "))
        masc6 = int(input("Quantas máscaras o posto 6 produziu? "))    
        p6 = int(input("Quantos cm de tecido o posto 6 gastou? "))
        print("\n----------------------------")

        maiorNumMascaras(masc1, masc2, masc3, masc4, masc5, masc6, mascaras)
        maisTecido(p1, p2, p3, p4, p5, p6, cmTecido)
        
        pronto = 1
    except ValueError:
        print("Dado inválido. Tente novamente!")