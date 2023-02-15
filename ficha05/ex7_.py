# gera senha baseada no username inserido

def generatePasswword(username):
    import random
    password = " "
    for i in range (1, len(userName), 2):
        password+= userName[i] + str(random.randint(1,9))
    password += str(len(userName))
    return password

userName = input("Username: ")
password1 = generatePasswword(userName)
print("Password: {0}" .format(password1))
