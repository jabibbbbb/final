
lista = []

for i  in range(4):
    nombre = input("ingrese el nombre:")
    nota = float(input("ingrese la nota:j"))

    usuario = {"nombre": nombre, 
           "nota" : nota}
    
    lista.append(usuario)

print(lista)

