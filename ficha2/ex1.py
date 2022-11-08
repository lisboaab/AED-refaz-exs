# determina se um dado número é par ou ímpar
try:
    numero = int(input("Insira um número inteiro:"))
except ValueError:
    print("O número inserido não é válido! Tente novamente.")

if numero % 2 == 0:
        print(f"O número {numero} é par!")
else:
        print(f"O número {numero} é ímpar!")

