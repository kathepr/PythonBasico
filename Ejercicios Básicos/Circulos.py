import math

radio=int(input("Ingrese el radio: "))
perimetro = 2 * math.pi * radio
area = math.pi * radio**2

print(f"Perimetro: {perimetro}")
print(f"Área: {area}")