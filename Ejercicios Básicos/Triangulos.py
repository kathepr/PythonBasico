a = float(input("\nIngrese a: "))
b = float(input("Ingrese b: "))
c = float(input("Ingrese c: "))

if a > b+c or b> a+c or c> a+b: 
    print ("El triangulo es invalido.")

elif a == b and a == c:
    print ("El triangulo es equilatero")

elif a==b or a==c or b==c:
    print ("El triangulo es isosceles")

elif a != b and a!=c and b!= c:
    print("El triangulo es escaleno")