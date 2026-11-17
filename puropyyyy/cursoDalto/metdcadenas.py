cadena1 = "holasoyjabibbbbbbb"
cadena2 = "bienvenidocrackkk"

#convierte a minuscula
minus= cadena1.lower()

#convierte a mayuscula
mayus = cadena1.upper()

#primera letra en mayuscula
prime = cadena1.capitalize()

#buscamos una cadena en otra cadena(enumera en en que posicion esta la letra o palabra que buscas)(si no hay coincidencia se vuelve -1)
busqueda_find = cadena1.find("v")

#buscamos una cadena en otra cadena(igual solo que al buscar datos y no encuentra nada me da error, o sea la coincidencia)
busqueda_index = cadena1.index("")

#si es numerico devuelve true. si no devuelve false
es_numerico = cadena1.isnumeric()

#si es alfa numerico devolvemos true, sino devolvemos false
alfanum = cadena1.isalpha()

#buscamos una cadena en otra cadena, devuelve la cantidad de veces que coincida
contar_coincidencia = cadena1.count("J")

#contar cuantos caracteres hay en una cadena
contar_caracteres = len(cadena1)


print(contar_caracteres)