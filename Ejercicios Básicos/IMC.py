edad = int(input("\nIngrese su edad: "))
altura = float(input("Ingrese su estatura en metros: "))
peso = float(input("Ingrese su peso en kilogramos: "))

IMC = (peso)/(altura**2)

if IMC < 22.0 and edad <45:
    print("\nEl riesgo de sufrir enfermedades coronarias es BAJO")
elif IMC < 22.0 and edad >=45:
    print("\nEl riesgo de sufrir enfermedades coronarias es MEDIO")
elif IMC >= 22.0 and edad <45:
    print("\nEl riesgo de sufrir enfermedades coronarias es MEDIO")
elif IMC >= 22.0 and edad >=45:
    print("\nEl riesgo de sufrir enfermedades coronarias es ALTO")