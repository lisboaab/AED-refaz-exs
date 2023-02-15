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
    



