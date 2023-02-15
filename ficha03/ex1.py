# leia 10 números e no final indique o maior e a média

from cmath import inf
import math

numeros = []
maior = -math.inf
pronto = 0

while pronto != 1:
    try:
        for i in range(1,11):
            numero = int(input("Insira o {}º número: " .format(i)))
            numeros.append(numero)
            if numero > maior:
                maior = numero
            pronto = 1
    except ValueError:
        print("Ocorreu um erro. Insira um valor válido!")

media = sum(numeros)/10
print(f"\n\t A média dos números é {media}")

print(f"\t O maior número é {maior}")