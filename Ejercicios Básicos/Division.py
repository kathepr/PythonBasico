dividendo=int(input("Dividendo: "))
divisor=int(input("Divisor: "))

cociente = dividendo // divisor
resto = dividendo % divisor

if dividendo % divisor==0:
    print("La división es exacta")
    print(f"Cociente: {cociente}")
    print(f"Resto: {resto}")

elif dividendo % divisor != 0:
    print("La división NO es exacta")
    print(f"Cociente: {cociente}")
    print(f"Resto: {resto}")

    