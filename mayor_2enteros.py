# Programa para verificar cual de dos numeros enteros es el mayor 

print("------------------------------------------")
print("------------MAYOR 2 ENTEROS:--------------")
print("------------------------------------------")

# input
x = int(input("digite el valor de x: "))
y = int(input("digite el valor de y: "))

#processing
if x == y:
    # output
    print ("Los numeros son iguales...")
else:
    if x > y:
        mayor = y

    else:
        mayor = y
         # output
        print ("El mayor entre " + str(x) + " y " + str(y) + " es " + str(mayor))
