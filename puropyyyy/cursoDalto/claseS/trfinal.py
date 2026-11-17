libros = []
usuarios = []
prestamos = []

multaxdia = 5000

def libro ():
    print("\n Registrar libro" ) 

    titulo = input("ingrese el titulo del libro:")
    autor = input("ingrese el autor:")

    if titulo == "" or autor == "":
        print("No se puede dejar los datos vacios")

    else:
        libro = {
            "titulo" : titulo,
            "autor" : autor,
            "disponible" : True
    }

    libros.append(libro)
    print("Libro registrado")

def registrarUsuario ():
    print("\n REGISTRAR USUARIO")    

    nombre = input("Nombre del usuario:")
    documento = input ("Documento:")

    if nombre == "" or documento == "":
            print("Debes completar los datos.")

    else:
         usuario = {
              "nombre" : nombre,
              "documento" : documento
         }
    usuarios.append(usuario)
    print("Usuario Registrado.")        

def MostrarLibros ():
     print("\n LISTA DE LIBROS")

     if len(libros) == 0:
          print("No hay libros registrados")

     else:
          for libro in libros:
            print("titulo:", libro["titulo"])
            print("autor:", libro["autor"])
            print("disponible:", libro["disponible"])


def PrestarLibro():
    titulo = input("¿Qué libro deseas prestar?:")

    for libro in libros:
        if libro["titulo"] == titulo:

            if libro["disponible"]:
                libro["disponible"] = False

                prestamos.append(titulo)

                print("Préstamo realizado correctamente.")

            else:
                print("El libro ya está prestado.")

            return

    print("El libro no existe.")
        

def DevolverLibro ():
    titulo = input("Nombre del libro que vas a devolver:")    

    if titulo in prestamos:

         dias = int(input("Dias de retraso:"))     

         multa = dias * multaxdia

         prestamos.remove(titulo)

         for libro in libros:
              if libro["titulo"] == titulo:
                   libro["disponible"] = True

         print("Libro devuelto correctamente")
         print("Multa a pagar: $", multa)

    else:
         print("Ese libro no tiene un prestamo activo.")

def menu ():

    while True: 

        try:
            print("\n===== BIBLIOTECA =====")
            print("1. Registrar libro")
            print("2. Registrar usuario")
            print("3. Mostrar libros")
            print("4. Prestar libro")
            print("5. Devolver libro")
            print("6. Salir")

            opcion = input("Seleccione una opcion:")

            if opcion == "1":
                 libro()

            elif opcion == "2":
                 registrarUsuario()

            elif opcion == "3":
                 MostrarLibros()

            elif opcion == "4":
                 PrestarLibro()

            elif opcion == "5":
                 DevolverLibro()    

            elif opcion == "6":
                 print("Hasta pronto.")

            else:
                 print(" Opcion incorrecta.")

                 break
             

        except ValueError:
             print(" Error: debes ingrsar datos numericos que correspondan a las opciones dadas.")


         
menu()

     
