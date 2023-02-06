import os

pasta = 'files'
ficheiro = 'files\paises.txt'

def inserir_paises():
    global ficheiro
    pais = str(input("País \t: ")).lower()
    continente = str(input("Continente \t: ")).lower()
    f = open(ficheiro, "r", encoding='utf=8')
    arquivo = f.read()
    if arquivo.find(pais) == -1:
        f.close()
        f = open(ficheiro, "a", encoding='utf-8')
        linha = pais + ';' + continente
        f.write(linha)
        f.write('\n')
        f.close()
    else:
        print("O país {0} já existe no ficheiro" .format(pais))
        input()

def cabecalho():
    print("País \t Continente")
    print("----------------------------")


def consultar_paises():
    global ficheiro

    cabecalho()
    pagina = 1
    lin = 1

    f = open(ficheiro, "r", encoding='utf-8')
    linhas = f.readlines()
    f.close()
    for linha in linhas:
        if lin == 11:
            input("Pág. {0}. Prima <enter> para continuar" .format(pagina))
            pagina+=1
            lin=1
            cabecalho()
        campos = linha.split(";")
        if len(campos[0]) < 6:
            campos[0]+= '\t'
        print("\t\t", campos[0], "\t", campos[1])
        lin+=1
    input()

def consultar_por_continente():
    global ficheiro
    continente = str(input("Insira um continente para busca: "))

    cabecalho()
    pagina = 1
    lin = 1

    continente = continente + "\n"
    f = open(ficheiro, "r", encoding='utf-8')
    linhas = f.readlines()
    f.close()
    for linha in linhas:
        if lin == 11:
            input("Pág. {0}. Prima <enter> para continuar" .format(pagina))
            pagina+=1
            lin=1
            cabecalho()
        campos = linha.split(";")
        if continente == campos[1]:
            if len(campos[0]) < 6:
                campos[0]+= '\t'
            print("\t\t", campos[0], "\t", campos[1])
            lin+=1
    input()

def paises_por_continente():
    global ficheiro
    continentes = ["europa", "ásia", "áfrica", "américa", "oceania"]
    aparicoes = []
    while len(aparicoes) < 5:
        for i in continentes:
            f = open(ficheiro, "r", encoding='utf-8')
            linhas = f.readlines()
            print(linhas)
            for linha in linhas:
                num = linha.count(i + '\n') # conta o número de aparições do continente na lista, que estão associados a um país único
            aparicoes.append(num)
    f.close()
    for i in range(len(continentes)):
        print("{0}: {1} países" .format(continentes[i], aparicoes[i]))
    input()

# cria pasta e ficheiro se eles não existem

if not os.path.exists(pasta):
    os.mkdir(pasta)
if not os.path.exists(ficheiro):
    f = open(ficheiro, "x")

again = 'S'
while again == 'S':
    os.system("cls")
    print("\t Menu \n1 - Inserir países \n2 - Consultar países \n3 - Consulta por continente\n4 - Consulta número de países\n0 - Sair")
    cmd = int(input("Escolha uma das opções: "))
    if cmd == 1:
        inserir_paises()
    elif cmd == 2:
        consultar_paises()
    elif cmd == 3:
        consultar_por_continente()
    elif cmd == 4:
        paises_por_continente()
    elif cmd == 0:
        again = 'N'
