def reverseStr(str):
    palavras = []
    div = str.split(" ")
    for i in div:
        palavras.append(i)
    palavras.reverse()
    for palavra in palavras:
        print (palavra, end=" ")

    mais_repetida = ""
    mais_repetida_contagem = 0
    for palavra in palavras:
        contagem = palavras.count(palavra)
        if contagem > mais_repetida_contagem:
            mais_repetida = palavra
            mais_repetida_contagem = contagem
    print("\nPalavra mais repetida:", mais_repetida)

str= "Este exercício de AED é um exercício do exame"
reverseStr(str)