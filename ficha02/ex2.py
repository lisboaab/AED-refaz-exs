# classifica um triângulo lendo as medidas dos 3 lados

pronto = 0
while  pronto != 1: 
    try: 
        lado1 = int(input("Insira o lado 1 do seu triângulo: "))
        lado2 = int(input("Insira o lado 2 do seu triângulo: "))
        lado3 = int(input("Insira o lado 3 do seu triângulo: "))
        pronto = 1
    except ValueError:
        print("Dado inserido inválido. Insira um número inteiro e positivo.")


try: 
    if lado1 == lado2 == lado3:
        print("O seu triãngulo é equilátero")
    elif lado1 == lado2 or lado2 == lado3 or lado1 ==lado3:
        print("O seu triâgulo é isósceles")
    else:
        print("O seu triangulo é escaleno")
except NameError:
    print("Dado inserido inválido. Insira um número inteiro e positivo.")