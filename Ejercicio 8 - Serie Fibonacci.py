#Algortimo para generar serie fibonacci
num1 = 1
num2 = 1

i = 0

while i <= 10:
    i += 1

    num1 += num2
    num2 += num1

    print (num1,num2, end=" ")    

print ("\n")
print ("Fin.")