caracter = input("\nIngrese caracter: ")

if caracter.isalpha():
    if caracter.isupper():
        print("Es una letra mayúscula\n")
    elif caracter.islower():
        print("Es una letra minúscula\n")
elif caracter.isdigit():
    print("Es un número\n")
else: 
    print("No es letra ni número\n")