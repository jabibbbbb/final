datos = [
    "Carlos",
    18,
    1.75,
    True,
    "Colombia",
    25,
    3.14,
    False,
    "Programación",
    100
]
datos.append(5)#inserta a la ultima posicion de la fila
datos[2]=0 #sustituir ( editar)
datos.insert(1,5)# inserta dato en la posicion que tu quieras primero la posicion y luego el dato
datos.pop()#borra el ultimo de la lista y si quieres mandas la posicion que quieres borrar(borra por posicion sirve para cuando solo tengas el numero de la posicion)
#si quieres eliminar el ultimo pones -1 y el anteultimo -2 y asi sucesivamente
datos.remove()# borra lo mismo que el pop pero no con posicion de la lista si no por el dato
datos.extend([])#insertar varios datos, pero hay que pasarlo como una lista tambien
datos.clear()#elimina todos los datos de la lista
print(datos)
