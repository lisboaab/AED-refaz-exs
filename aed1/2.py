# pequeno simulador do esforço cardíaco

# erro: se coloca isso dps do while printa fim direto sem nem correr o programa     
#  if novosDados.upper() == "N" or "n":   
   #     print("\nFim\n")
    #    break

novosDados = "S"
novosDados = novosDados.upper()

while novosDados.upper() == "S":

    genero = input("Insira o seu género (M/F): ")
    genero = genero.upper()
    idade = int(input("Insira a sua idade: "))
    frequenciaCardiaca = int(input("Indique a sua frequência cardíaca: "))
    if genero == "F":
        fcm = 226 - idade
        print("Sua Frequência Cardíaca Máxima é {}" .format(fcm))
    elif genero == "M":
        fcm = 220 - idade
        print("Sua Frequência Cardíaca Máxima é {}" .format(fcm))
    else:
        print("Insira um dado válido. M ou F") 

    print("------")
    if (50 * fcm) /100 < frequenciaCardiaca < (60 * fcm) /100:
        print("Sua atividade física é moderada")
    elif  (61 * fcm) /100 < frequenciaCardiaca < (70 * fcm) /100:
        print("Sua atividade física é estilo treino de resistência")
    elif  (71 * fcm) /100 < frequenciaCardiaca < (80 * fcm) /100:
        print("Sua atividade física é aeróbica")
    elif  (81 * fcm) /100 < frequenciaCardiaca < (90 * fcm) /100:
        print("Sua atividade física é anaeróbica")
    else:
        print("Sua atividade física é considerada Red Zone")
    novosDados = str(input("Deseja indicar novos dados (S/N)? "))
    