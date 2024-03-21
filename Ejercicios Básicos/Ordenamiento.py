
#Programa 1: 
def OrdenDosNumeros(n1,n2):
    lista = [num1, num2]
    listaOrdenada = sorted(lista)

    print("\nEl orden de los números de menor a mayor es: ")
    for i in listaOrdenada:
        print(i, end="  ")
    print("\n")


#Programa 2: 
def OrdenTresNumeros(n1,n2,n3):
    lista2 = {num1, num2, num3}
    listaOrdenada2 = sorted(lista2)

    print("\nEl orden de los números de menor a mayor es: ")
    for i in listaOrdenada2:
        print(i, end="  ")
    print("\n")

#Programa 3:
def OrdenCuatroNumeros(n1,n2,n3,n4):

    lista3 = {num1, num2, num3,num4}
    listaOrdenada3 = sorted(lista3)

    print("\nEl orden de los números de menor a mayor es: ")
    for i in listaOrdenada3:
        print(i, end="  ")
    print("\n")




print("""

********************************
      OPCIONES DE PROGRAMA
********************************
1. Programa que recibe la entrada de 2 números y los ordena
2. Programa que recibe la entrada de 3 números y los ordena
3. Programa que recibe la entrada de 4 números y los ordena

""")
opcion = int(input("Ingrese la opción que desea ver: "))
if opcion == 1:
    num1 = int(input("\nIngrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    OrdenDosNumeros(num1, num2)
elif opcion == 2:
    num1 = int(input("\nIngrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    num3 = int(input("Ingrese el tercer número: "))
    OrdenTresNumeros(num1, num2, num3)
elif opcion == 3:
    num1 = int(input("\nIngrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    num3 = int(input("Ingrese el tercer número: "))
    num4 = int(input("Ingrese el cuarto número: "))
    OrdenCuatroNumeros(num1, num2, num3, num4)