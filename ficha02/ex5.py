# le 3 números e os imprima por ordem crescente

pronto = 0
while pronto != 1:
    try:
        num1 = int(input("1. Insira um número: "))
        num2 = int(input("2. Insira um número: "))
        num3 = int(input("3. Insira um número: "))
        pronto = 1
    except ValueError:
        print("Insira um valor válido!")

if num1 > num2 > num3:
    print("{0}, {1}, {2}" .format(num3, num2, num1))
if num1 > num3 > num2:
    print("{0}, {1}, {2}" .format(num2, num3, num1))
if num2 > num1 > num3:
    print("{0}, {1}, {2}" .format(num3, num1, num2))
if num2 > num3 > num1:
    print("{0}, {1}, {2}" .format(num1, num3, num2))
if num3 > num1 > num2:
    print("{0}, {1}, {2}" .format(num2, num1, num3))
if num3 > num2 > num1:
    print("{0}, {1}, {2}" .format(num1, num2, num3))