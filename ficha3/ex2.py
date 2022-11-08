# le n números e no final indica o maior e a média

from cmath import inf
import math

numeros = []
maior = -math.inf
pronto = 0

while pronto != 1:
    try:
        numerosAler = int(input("Quantos números deseja ler? "))
        for i in range(numerosAler):
            numero = int(input("Insira o {}º número: " .format(i+1)))
            numeros.append(numero)
            if numero > maior:
                maior = numero
            pronto = 1
    except ValueError:
        print("Ocorreu um erro. Insira um valor válido!")

media = sum(numeros)/10
print(f"\n\t A média dos números é {media}")

print(f"\t O maior número é {maior} \n")