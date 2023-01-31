"""
Elabore um programa que permita ler a faturação mensal de uma empresa ao longo
dos 12 meses do ano (de janeiro a dezembro).
O programa deve incluir a chamada de 3 funções que devolvam:
a) o mês de maior faturação
b) o mês de menor faturação
c) a média mensal de faturação
"""
meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

def maiorFaturacao(faturacoes):
    maiorFatuc = max(faturacoes)
    posicao = faturacoes.index(maiorFatuc)
    mes = meses[posicao]
    return mes

def menorFaturacao(faturacoes):
    menorFatuc = min(faturacoes)
    posicao = faturacoes.index(menorFatuc)
    mes = meses[posicao]
    return mes

def mediaMensalFaturacoes(faturacoes):
    return sum(faturacoes) / 12


faturacoes = []
for i in range(len(meses)):
    fat = int(input("Faturação do mês {0}: " .format(meses[i])))
    faturacoes.append(fat)

maiorFat = maiorFaturacao(faturacoes)
menorFat = menorFaturacao(faturacoes)
mediaFat = mediaMensalFaturacoes(faturacoes)

print("O mês de maior faturação foi: {0}" .format(maiorFat))
print("O mês de menor faturação foi: {0}" .format(menorFat))
print("A média mensal de faturações é: {0}" .format(mediaFat))