# calcula o peso ideal

altura = input("Insira a sua altura em cm: ")

try:
    peso_ideal = (int(altura)-100) * 0.9
except ValueError:
    print("O numero inserido é inválido. Insira um número inteiro como altura.")
else:
    print("Ocorreu um erro. Tente novamente!")

print (f"O seu peso ideal é {peso_ideal}")