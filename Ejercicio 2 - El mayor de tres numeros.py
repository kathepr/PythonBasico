num1 = input ("INGRESE EL NUMERO 1 ")
num2 = input ("INGRESE EL NUMERO 2 ")
num3 = input ("INGRESE EL NUMERO 3 ")

if num1>num2 and num1>num3:
    print ("El número mayor es el primer número:", num1)

elif num2>num1 and num2>num3:
    print ("El número mayor es el segundo número:", num2)

else:
    print ("El número mayor es el tercer número:", num3)