#Algortimo para verificar si un número es primo

num = int(input("Ingrese un número: "))
divisor = 0
contador = 0


while divisor <= num:
    divisor+=1

    if num % divisor == 0:
     contador += 1
    


if contador==2:
        print ("El número es primo")
else:
        print ("El número no es primo")   