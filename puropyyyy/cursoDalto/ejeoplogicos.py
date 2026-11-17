while True:
    parcial1 = int(input("Ingrese la nota 1: "))
    parcial2 = int(input("Ingrese la nota 2: "))
    if parcial1 >= 5 or parcial2 >= 5 or parcial1 < 1 or parcial2 < 1:
        print("Error: las notas deben estar entre 1 y 5")
    elif parcial1 >= 3 and parcial2 >= 3:
        print("no hace parcial")
        break
    else:
        print("si hace parcial 3")
        break
