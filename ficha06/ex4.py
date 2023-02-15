"""
Altere o programa anterior de modo a incluir também a leitura dos nomes dos participantes no concurso.
A função positiveList deve agora devolver duas listas: uma com pontuações e outra
com nomes dos participantes que obtiveram pontuações positivas (>=10)
"""

def positiveList(nomes, notas):
    notasPositivas = []
    nomesPositivos = []
    for i, nota in enumerate(notas):
        if nota >= 10:
            notasPositivas.append(nota)
            nomesPositivos.append(nomes[i])
    return notasPositivas, nomesPositivos

listaNotas = []
listaNomes = []
for i in range(10):
    nome = input("Nome {0}: ".format(i + 1))
    listaNomes.append(nome)
    nota = int(input("Pontuacao {0}: ".format(i + 1)))
    listaNotas.append(nota)

resultado = positiveList(listaNomes, listaNotas)
print(resultado)
