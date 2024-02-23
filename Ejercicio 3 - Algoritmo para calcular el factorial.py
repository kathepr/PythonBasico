num = int (input ("Ingrese el número al que desea calcularle el factorial "))

factorial=1
for i in range(1, num+1): #Va de 1 hasta el num+1 , hay que poner +1 porque "range" siempre pone un numero menos 
    
    factorial*=i #factorial* significa que estoy multiplicando factorial * i y luego asignando el resultado a "factorial"
    
print ("El factorial de", num, "es =", factorial)
 