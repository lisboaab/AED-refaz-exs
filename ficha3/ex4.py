# simule o jogo da adivinha de um número

import random

tentativas = 0
numero = random.randint(1, 50)
tentativaUsuario = int(input("Insira um número: "))
for tentativaUsuario in range(10):
    if tentativaUsuario > numero:
        print("Tente um numero menor")
        tentativas += 1
    elif tentativaUsuario < numero:
        print("Tente um número maior!")
        tentativas += 1
    elif tentativas == 10:
        print("Você esgotou suas tentativas!")
        break
    else:
        print("Você acertou o palpite! Você conseguiu em {} tentativas" .format(tentativas))
        break
