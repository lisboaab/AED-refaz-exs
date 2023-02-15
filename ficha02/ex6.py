# m pequeno simulador de esforço cardíaco, quando um atleta desenvolve atividade física

pronto = 0
while pronto != 1:
    try:
        genero = input("Qual o seu género? (F/M) ")
        idade = int(input("Qual a sua idade: "))
        genero = genero.upper()
        pronto = 1
    except ValueError:
        print("Ocorreu um erro. Insira válidos!")


if genero == "F":
    fcm = 226 - idade
    print(f"Sua frequência cardíaca máxima é {fcm}")
elif genero == "M":
    fcm = 220 - idade
    print(f"Sua frequência cardíaca máxima é {fcm}")