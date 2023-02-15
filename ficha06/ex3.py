"""
Crie um programa que leia a pontuação de 10 participantes num concurso de programação (a pontuação deve 
estar validada entre 0 a 20, por uma estrutura try-except). O programa deve invocar uma função, positiveList 
que receba a lista das 10 pontuações e devolva uma nova lista apenas com as pontuações positivas (>=10).
"""

def positiveList(lista):
    notasPositivas = []
    for nota in lista:
        if nota >= 10:
            notasPositivas.append(nota)
    return notasPositivas

listaNotas = []
for i in range(10):
    try:
        nota = int(input("Pontuacao {0}: " .format(i + 1)))
        if nota < 0 or nota > 20:
            raise ValueError()
    except ValueError:
        print("Nota inserida é inválida, tente novamente")
    except:
        print("Ocorreu um erro, tente novamente!")
    else:
        listaNotas.append(nota)

notasPositivas = positiveList(listaNotas)
print(f"As notas positivas foram: {notasPositivas}")