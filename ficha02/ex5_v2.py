# le 3 números e os imprima por ordem crescente
'''
num = input("Insira um número: ")
            numeros.append(num)
            print(numeros)
    except:
        print("errito") 
'''

numeros = []
pronto = 0
while pronto != 1:
    try:
        num1 = int(input("1. Insira um número: "))
        num2 = int(input("2. Insira um número: "))
        num3 = int(input("3. Insira um número: "))
        numeros.append(num1)
        numeros.append(num2)
        numeros.append(num3)
        pronto = 1
        print(numeros)
    except ValueError:
        print("Insira um valor válido!")
            

# continuar...
if num1 > num2 and num1 > num3:
    num1 = numeros[2]
    print(numeros)