# gera senha baseada no username inserido

def generatePasswword(username):
    import random
    numero = random.randint(0,10)
    password = username[0] + numero + username[2] + numero 

input username
username = posicoes pares do username intercalados com numeros 
gerados aleatoriamente e termina com o mesmo numero de caracteres do username
