from time import localtime


def age(nacimiento, fechaActual):
    diaNa, mesNa, añoNa = nacimiento
    diaA, mesA, añoA = fechaActual

    edad = añoA - añoNa
    if (mesA, diaA) < (mesNa, diaNa):
        edad -=1
    return edad




nacimiento = int(input("\n¿Que día nació? ")), int(input("¿En que mes nació? ")), int(input("¿En que año es nació? "))
t = localtime()
fechaActual = (t.tm_mday, t.tm_mon, t.tm_year)

edad = age(nacimiento, fechaActual)
print(f"La edad actual es: {edad} años\n")

