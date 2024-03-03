#Area de un circulo

import math   #import se utiliza para incluir módulos o paquetes en el programa
              #Con import le permito al programa acceder a todo lo que contiene el módulo o paquete

print ("Vamos a calcular el área de un circulo: \n")

radio = int(input("Ingrese la medida del radio: "))
pi = math.pi 

area = pi * radio**2

print ("El área del circulo es de: ", round(area,2))
