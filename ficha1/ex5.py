#  partir de um determinado número de segundos calcula o número de horas, minutos e segundos correspondentes

print("Dica: insira um número grande. Ex.: >1000")
segundos1 = int(input("Insira um numero em segundos: "))

horas = segundos1 / 3600 
minutos = (segundos1 % 3600)/60
segundos = (segundos1 % 3600) % 60

print(f"{int(segundos1)} segundos é igual a {int(horas)} hora(s), {int(minutos)} minuto(s) e {int(segundos)} segundo(s)")