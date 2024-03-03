t=int(input("\nHora actual: "))
h=int(input("Cantidad de horas: "))

hora_futura = (h + t) % 12 #residuo

print(f"En {h} horas, el reloj marcara las {hora_futura}")