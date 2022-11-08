# Considere uma fábrica que dispõe de uma linha de produção de máscaras, constituída por 6 postos de trabalho.
# Implemente um programa que leia, para cada posto de trabalho, a produção (nº de máscaras produzidas) e o tecido
# gasto (em cm).
# Com base nestes dados, implemente as seguintes funções:
# • Função que devolva os dois postos de trabalho que produziram maior número de máscaras
# • Função que devolva qual o posto de trabalho que gastou mais tecido

def maiorNumMascaras (p1, p2, p3, p4, p5, p6, maior, mascaras):
    for postos in range(1-7):
        mascaras = int(input("Quantas máscaras o posto {} produziu? " .format(postos)))    #trocar postos por i se n funcionar
        print(mascaras)

def maisTecido (p1, p2, p3, p4, p5, p6, cmTecido):
    for postos in range(1-7):
        int(input("Quantos cm de tecido o posto {} gastou? " .format(postos)))
        print(postos)



mascaras = int(input("Quantas máscaras o posto 1 produziu? "))    #trocar postos por i se n funcionar
print(mascaras)