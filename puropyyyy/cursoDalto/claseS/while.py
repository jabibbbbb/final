#el while es un ciclo para repetir un bloque de codigo de froma indefinida no como el "for" que es hasta cuando uno mismo diga
user="admin"
password=""
contrasena_verdaadera =123

while contrasena_verdaadera != password:
    password =int(input("ingresa tu contrasena"))

    if password != contrasena_verdaadera:
        print("contrasena incorrecta")

print("bienvenido")    