# simule o jogo da adivinha de um número

import random

tentativas = 1
numero = random.randint(1, 50)
tentativaUsuario = int(input("Insira um número: "))
while numero != tentativaUsuario and tentativas < 10:
    if tentativaUsuario > numero:
        print("Tente um numero menor")
    elif tentativaUsuario < numero:
        print("Tente um número maior!")
    tentativas += 1
    tentativaUsuario = int(input("Insira um número: "))
    if tentativas == 10:
        print("Você esgotou suas tentativas!")
        break

if numero == tentativaUsuario:
    print("Você acertou o palpite! Você conseguiu em {} tentativas" .format(tentativas))
else:
    print("Você esgotou suas tentativas!")
