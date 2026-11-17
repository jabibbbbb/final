import random
secreto = random.randint(1,5)
numero = int(input("adivina el numero entre 1 y 5"))
while numero != secreto:
  print("incorrecto")

  numero = int(input("ingrese el numero"))


print("adivinaste el numero")