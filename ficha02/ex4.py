# calcula indice de massa corporal e classifica

pronto = 0
while pronto != 1:
    try:
        peso = float(input("Insira o seu peso em kg: "))
        altura = float(input("Insira a sua altura em metros: "))
        pronto = 1
    except ValueError:
        print("Dado inválido. Tente novamente!")

try:
    imc = peso / (pow(altura,2))
    print("Seu IMC aproximado é: {:.2f}" .format(imc))
except ZeroDivisionError:
    print("Altura inválida. Tente novamente!")
except NameError:
    print("Ocorreu um erro, tente novamente")


if imc < 18.5:
    print("Tu estás abaixo do peso")
elif imc>=18.5 and imc<25:
    print("Estás saudável!")
elif imc>=25 and imc<30:
    print("Estás em sobrepeso!")
elif imc>=30 and imc<35:
    print("Estás com obesidade grau 1!")
elif imc>=35 and imc<40:
    print("Estás com obesidade grau 2 (severa)!")
elif imc>=40:
    print("Estás com obesidade grau 3 (mórbida)!")


