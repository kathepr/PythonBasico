certamen1=int(input("Ingrese la nota del certamen 1: "))
certamen2=int(input("Ingrese la nota del certamen 2: "))
laboratorio=int(input("Ingrese la nota del laboratorio: "))

certamen3 = (((60 - (laboratorio*0.3))*3)/0.7) - certamen1 - certamen2

print(f"Necesita nota {certamen3} en el certamen 3")