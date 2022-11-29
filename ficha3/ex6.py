# gerar um número aleatório entre 1900 e 2020, número esse que representa um ano. 
# Considerando o ano gerado aleatoriamente, pretende-se que o programa indique se o ano é bissexto ou não.

import random

ano = random.randint(1900, 2000)
print ("O ano gerado foi: ", ano)
if ano % 4 == 0 and ano % 100 != 0:
    print ("O ano", ano, "é um ano bissexto!")
else:
    print ("O ano", ano, "não é bissexto")