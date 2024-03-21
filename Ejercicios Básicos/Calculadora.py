num1 = int(input("\nIngrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
operando = input("Ingrese un operando (+ , - , * , / ,  **): ")

if operando == "+":
    suma = num1 + num2
    print(f"El resultado de la suma de {num1} y {num2} es: {suma}\n")
elif operando == "-":
    resta = num1 - num2
    print(f"El resultado de la resta de {num1} y {num2} es: {resta}\n")
elif operando == "*":
    multiplicacion = num1 * num2
    print(f"El resultado de la multiplicación de {num1} y {num2} es: {multiplicacion}\n")
elif operando == "/":
    division = num1 / num2
    print(f"El resultado de la división de {num1} y {num2} es: {division}\n")
elif operando == "**":
    potencia = num1**num2
    print(f"El resultado de la suma de {num1} y {num2} es: {potencia}\n")