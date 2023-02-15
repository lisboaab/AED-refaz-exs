# simulador do peso ideal baseado no genero inserido pelo usuário

genero = str(input("Insira o seu género (M/F): "))
genero = genero.upper()

altura = int(input("Indique a sua altura (cm): "))

if genero == "F":
    pesoIdeal = (altura-100) - (altura-150) / 2
    print("Seu peso ideal é {:.2f}" .format(pesoIdeal))
elif genero == "M":
    pesoIdeal = (altura-100) - (altura-150) / 4
    print("Seu peso ideal é {:.2f}" .format(pesoIdeal))
else:
    print("Por favor, insira um dado válido. M ou F")