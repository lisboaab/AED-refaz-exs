import os
import random

def imprimePais():
    for char in range(len(paisSorteado)):
        char = "-"
    print(paisSorteado)




# -----------------------
file = ".\\ficha10\\ficheiros\\paises.txt"
pasta = "ficheiros"

if not os.path.exists(pasta):
    os.mkdir(pasta)

ficheiro = open(file, "r", encoding="utf-8")
listaPaises = ficheiro.readlines()
ficheiro.close()

paisSorteado = random.choice(listaPaises)

tentativas = 0
palpite = ""
numCaracteres=1

print("\t Adivinhe o pais!")
while tentativas <3 and palpite.upper() != paisSorteado.upper():
    imprimePais(paisSorteado, numCaracteres)
    palpite = input("\n\n\t\tQual o país? ")
    numCaracteres+=1
    tentativas+=1
if palpite.upper() != paisSorteado.upper():
    print("\n\n\t\tGamne Over! :( :( :(")
else:
    print("\n\n\t\tParabéns, acertou!!! :-)")