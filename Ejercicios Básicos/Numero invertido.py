num = input("Ingrese número entero de tres digitos: ")
num_invertido = ""

for character in num:
    num_invertido = character + num_invertido


print(f"Número invertido: ",num_invertido)