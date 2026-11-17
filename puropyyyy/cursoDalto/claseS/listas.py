l = [14, 25, 42, 31, 19, 8, 50, 73, 11, 22]
pares = []
impares = []

for q in l:
    if q %  2 == 0:
        pares.append(q)
    else:
        impares.append(q)    

print("numeros pares:", pares)        
print("cantidad de pares", len(pares))

print("numeros impares:", impares)        
print("cantidad de impares", len(impares))
#len sirve para contar cuantos elementos hay en  una lista