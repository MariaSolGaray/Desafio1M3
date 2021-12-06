lista = []

print ("Ingrese 15 números a continuación")

for x in range(15):
    lista.append(int(input("Número: ")))

print ("Mayor: ",(max(lista)))
print ("Menor: ",(min(lista)))
print ("La sumatoria de todos los numeros es de: ",sum(lista))
print ("El promedio de todos los numeros es de: ",sum(lista)/15)