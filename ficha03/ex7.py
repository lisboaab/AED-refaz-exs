# Elabore um programa que leia um número (inteiro e positivo) e indique se ele é primo ou não.
# Nota: Um número primo é divisível apenas por si próprio e por 1


'''
codigo abaixo não dá certo por exemplo com o numero 15, que não é divisível por 2 mas também não é primo
numero = int(input("Insira um número: "))
if numero < 0:
    print("Insira um número inteiro e positivo")
elif numero % 2 == 0:
    print ("O numero", numero, "não é um número primo")
else:
    print("O numero", numero, " é um número primo")
'''
numero = int(input("Insira um número: "))

primo = True
for i in range(2, numero):  # o range varia entre 2 e o numero-1
    resto = numero % i      # resto é igual ao numero inserido dividido pelo numero do range(i) -> no caso a primeira tentativa sera 2, depois 3 ...
    if resto == 0:          # se encontrar um resto 0  ....
        primo = False       # então o número não é primo
        break

if primo==True:
    print("O numero", numero, "é primo")
else:
  print("O numero", numero, "não é primo")
