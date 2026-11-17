
while True:
    try:
        usuario = int(input("Ingrese su usuario: "))
        contrasena = int(input("Ingrese su cedula: "))

        if contrasena == 123456:
            print("Bienvenido")
            break
        else:
            print("Contraseña incorrecta. Intente nuevamente.")

    except ValueError:
        print("El usuario y la cedula deben ser numeros enteros.")

