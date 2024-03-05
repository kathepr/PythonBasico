palabra1 = input("\nPalabra 1: ")
palabra2 = input("Palabra 2: ")

longitud1 = len(palabra1)
longitud2 = len(palabra2) 

if longitud1>longitud2:
    diferencia = longitud1 - longitud2
    print(f"La palabra {palabra1} tiene {diferencia} letras más que {palabra2}")

elif longitud2>longitud1:
    diferencia = longitud2 - longitud1
    print(f"La palabra {palabra2} tiene {diferencia} letras más que {palabra1}")

else:
    print("Las dos palabras tienen el mismo largo")
