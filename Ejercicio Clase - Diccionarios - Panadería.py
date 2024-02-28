#Crear diccionario de pan dulce con sus respectivos valores

Salado={"Baguete":4000,
          "Croissant":2500,
          "Pan Integral":6000,
          "Pan de Yuca":1500,
          "Pan de Bono":1200,
          "Almojabana":1000,
          "Pastel de Pollo":5000,
          "Pan de ajo":2500,
          "Palito de queso":800,
          "Empanada":2000
          }

Postres={"Torta de Chocolate":25000,
         "Cheesecake de fresa": 30000,
         "Tarta de limón":20000,
         "Tiramisú":18000,
         "Trufas":2000,
         "Brownies":5000,
         "Rollo de Canela":4000,
         "Merengues":2500,
         "Crepe de nutella":15000,
         "Alfajor": 5000
         }

Bebidas={"Tinto":2000,
         "Aguapanela":2000,
         "Milo":2500,
         "Jugo de naranja": 8000,
         "Limonada": 6000,
         "Cerveza Aguila":8000,
         "Agua sin gas": 3000,
         "Chocolate caliente": 3500,
         "Té caliente":3500,
         "Té helado":3500
         }

items_Salado =(f"{Salado.keys()} {Salado.values()}")
keys_Salado = list(Salado.keys())
valor_Salado= list(Salado.values())


items_Postres =(f"{Postres.keys()} {Postres.values()}")
list_Postres = list(Postres.keys())
valor_Postres= list(Postres.values())

items_Bebidas =(f"{Bebidas.keys()}{Bebidas.values()}")
list_Bebidas = list(Bebidas.keys())
valor_Bebidas= list(Bebidas.values())



print("\n******************************************************")
print("\tBienvenido a la Panadería de Kathe")
print("******************************************************\n")

print("Tenemos las siguientes categorías de productos")
print("""
      1. Panadería Salada
      2. Postres
      3. Bebidas
      """)

opcion=int(input("Ingrese el número correspondiente a la opción que desea consultar: "))


#CONDICIONAL PARA OPCION 1 - PANADERIA SALADA
if opcion==1:
    print ("\n\tPANADERIA SALADA\n")
    for i,_ in enumerate (keys_Salado):  #Se colocó guión bajo porque no vamos a utilizar ese valor de la lista. 
        
        print(f"{i}.{keys_Salado[i]} = ${valor_Salado[i]}")

    opcion = int(input("\n¿Qué opción desea? "))
    print (f"\nUsted ha seleccionado '{keys_Salado[opcion]}', este producto tiene un valor de ${valor_Salado[opcion]}")

    #CREACIÓN DE PROMOCIONES PARA PANADERIA SALADA: 
    if opcion ==5:
        print (f"\n****************      ¡Hoy tenemos 2x1 en {keys_Salado[opcion]}!      ****************")
    elif opcion ==3:  
        print (f"\n****************      ¡Hoy tenemos {keys_Salado[opcion]} a mitad de precio!      ****************")  
    
    #PREGUNTAR POR NÚMERO DE UNIDADES A COMPRAR
    unidad=int(input(f"\n¿Cuantas unidades de {keys_Salado[opcion]} desea comprar? "))

    #PREGUNTAR CON CUANTO DINERO PAGA EL CLIENTE:  
    dinero = int(input("\nIngrese la cantidad de dinero disponible: ")) 
    totalDinero = dinero*unidad 
    
    #if keys_Salado[opcion] == 3:
    #    totalDinero = (dinero*unidad)/2

    
    vueltos= totalDinero - valor_Salado[opcion]

      
    #CONDICIONAL PARA VUELTOS:
    if dinero >= valor_Salado[opcion]:
        if opcion == 5:
            promo = unidad * 2
            print (f"\nUsted compró {unidad} unidades de {keys_Salado[opcion]}. Por nuestra promoción 2x1, le entregamos {promo} unidades.")
            print (f"\nEl total a pagar es ${totalDinero} y sus vueltos son: ${vueltos}")

        elif opcion == 3:
            totalDinero = (dinero*unidad)/2
            print (f"\nUsted compró {unidad} unidades de {keys_Salado[opcion]}. Por nuestra promoción a mitad de precio, el total a pagar es ${totalDinero} y sus vueltos son: ${vueltos}") 
        
        else:
             print(f"\nUsted compró {unidad} unidades de {keys_Salado[opcion]}. El total a pagar es ${totalDinero} y sus vueltos son {vueltos}")

    else:
        print(f"\nUsted desea {unidad} unidades de {keys_Salado[opcion]}. El total a pagar es ${totalDinero}, le falta un total de ${-vueltos}.")

        


        




