# leia uma frase e escreva os seus caracteres por ordem inversa.

texto = input("Insira sua frase: ")
tam = len(texto)
for i in range(tam-1, -1, -1):
    print(texto[i], end="")