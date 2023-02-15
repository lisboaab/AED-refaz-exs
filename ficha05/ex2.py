# leia uma frase e determine:
# • Número de caracteres
# • Número de espaços
# • Número de vogais

frase = input("Insira uma frase:")
espacos = frase.count(" ")
cacteres = len(frase)
vA = frase.count("a")
vE = frase.count("e")
vI = frase.count("i")
vO = frase.count("o")
vU = frase.count("u")
vogais = vA + vE + vI + vO + vU

print("O numero de caracteres é {0}" .format(cacteres))
print("O numero de espacos é {0}" .format(espacos))
print("O numero de vogais é {0}" .format(vogais))