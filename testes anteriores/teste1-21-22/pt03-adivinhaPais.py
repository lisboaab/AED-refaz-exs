import random

lPaises = ["Brasil", "Portugal", "Bélgica", "Alemanha", "França", "Hungria"]

def sortearPais():
    pos = random.randint(0, len(lPaises)-1)
    return lPaises[pos]


def imprimePais(paisAdivinhar, numCaracteres):
   i= numCaracteres
   texto = ""
   texto = paisAdivinhar[0:numCaracteres]
   while i < len(paisAdivinhar):
        texto +="_ "
        i+=1
   print("\n\t\t\t", texto)



def jogar(paisAdivinhar):
    tentativas = 0
    palpite = ""
    numCaracteres=1
    while tentativas < 3 and palpite.upper() != paisAdivinhar.upper():
        imprimePais(paisAdivinhar, numCaracteres)
        palpite = input("\n\n\t\tQual o país? ")
        numCaracteres+=1
        tentativas+=1
    if palpite.upper() != paisAdivinhar.upper():
        print("\n\n\t\tGame Over! :( :( :(")
    else:
        print("\n\n\t\tParabéns, acertou!!! :-)")


#-----------------------------------------
print("\n\t\t\tJOGO ADIVINHA O PAÍS")
print()
paisAdivinhar= sortearPais()
jogar(paisAdivinhar)
    