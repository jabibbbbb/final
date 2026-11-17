n1 = int(input("digte el primer numero "))
n2 = int(input("digite el segundo numero "))
opcion = 0

while opcion != 5:
  print("1. suma")
  print("2. resta")
  print("3. multiplicacion")
  print("4. division")

  opcion = int(input("introduce una opcion "))

  match opcion:
    case 1:
      print("resultado",n1 + n2)
      break
    case 2:
      print("resultado",n1 - n2)
      break
    case 3: 
      print("resultado",n1 * n2)
      break
    case 4:
            if n2 != 0:
                print("Resultado:", n1 / n2)
                break
            else:
                print("Error: no se puede dividir entre cero")
                
    case _:
      print("opcion no registrada")
      