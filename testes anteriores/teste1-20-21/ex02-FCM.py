def calcFCM(genero, idade, freqCard):
    result = 0
    if genero.upper() == "F":
        fcm = 226 - idade
        result = (100*freqCard)/fcm
    elif genero.upper() == "M":
        fcm = 220 - idade
        result = (100*freqCard)/fcm

    if result >= 50 and result <= 60:
        return "Atividade Moderada"
    elif result >= 61 and result <= 70:
        return "Treino de resistencia"
    elif result >= 71 and result <= 80:
        return "Nível aeróbico"
    elif result >= 81 and result <= 90:
        return "Nível anaeróbico"
    elif result >= 91 and result <= 100:
        return "RedZone"


def calcFCM(genero,idade,freqCard):
    result = 0
    if genero.upper() == "F":
        fcm = 226 - idade
        result = (100*freqCard)/fcm
    elif genero.upper() == "M":
        fcm = 220 - idade
        result = (100*freqCard)/fcm

    if result >= 50 and result <= 60:
        return "Atividade Moderada"
    elif result >= 61 and result <= 70:
        return "Treino de resistencia"
    elif result >= 71 and result <= 80:
        return "Nível aeróbico"
    elif result >= 81 and result <= 90:
        return "Nível anaeróbico"
    elif result >= 91 and result <= 100:
        return "RedZone"



resp = "S"
while resp.upper() == "S":
    genero = input("Qual seu gênero? (M/F)")
    genero = genero.upper()

    idade = int(input("Qual sua idade? "))

    freqCard = int(input("Qual sua frequência cardíaca? "))

    nivel_atividade = calcFCM(genero, idade, freqCard)

    print(nivel_atividade)

    resp = input("Deseja inserir novos dados? (S/N)")






""""""