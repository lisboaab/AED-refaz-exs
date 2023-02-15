# simulador do seu peso noutro Planeta

# quando o planeta escolhida da um numero errado, e o peso tbm aparece a msg do peso errado e n do planeta

import math
 
print("De acordo com a tabela abaixo, escolha um planeta para simular seu peso:")
print("\t 1. Mercúrio \n\t 2. Vénus \n\t 3. Marte \n\t 4. Júpiter \n\t 5. Saturno \n\t 6. Urano \n")

pronto = 0
while pronto!=1:
    try:
        planeta = int(input("Qual o número do planeta escolhido? "))
        pesoTerra = float(input("Qual é o seu peso atual? (kg) "))
        pronto = 1
    except ValueError:
        print("Valor inválido.")    
    
if pesoTerra < 0:
    print("Por favor, insira um peso real!")
elif planeta == 1:
    pesoPlaneta = pesoTerra * 0.37
    print ("O seu peso em Mercúrio seria {}" .format(math.ceil(pesoPlaneta)))
elif planeta == 2:
    pesoPlaneta = pesoTerra * 0.88
    print ("O seu peso em Vénus seria {}" .format(math.ceil(pesoPlaneta)))
elif planeta == 3:
    pesoPlaneta = pesoTerra * 0.38
    print ("O seu peso em Marte seria {}" .format(math.ceil(pesoPlaneta)))
elif planeta == 4:
    pesoPlaneta = pesoTerra * 2.64
    print ("O seu peso em Júpiter seria {}" .format(math.ceil(pesoPlaneta)))
elif planeta == 5:
    pesoPlaneta = pesoTerra * 1.15
    print ("O seu peso em Saturno seria {}" .format(math.ceil(pesoPlaneta)))
elif planeta == 6:
    pesoPlaneta = pesoTerra * 1.17
    print ("O seu peso em Urano seria {}" .format(math.ceil(pesoPlaneta)))
else:
    print("Por favor, insira um número de planeta válido!")