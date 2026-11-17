# la f significa : formatted, te deja meter variables dentro del texto sin hacer tantos lios (f-string  )
n1 = 12
import random

secreto = random.randint(1, 100)
vidas = 7

print("🎮 ADIVINA EL NÚMERO del 1 al 100")
print(f"Tienes {vidas} vidas\n")

while vidas > 0:
    intento = int(input("Tu número: "))
    
    if intento == secreto:
        print(f"¡GANASTE! Era el {secreto} 🎉")
        break
    elif intento < secreto:
        print("Más alto... 📈")
    else:
        print("Más bajo... 📉")
    
    vidas -= 1
    print(f"Te quedan {vidas} vidas\n")

if vidas == 0:
    print(f"Perdiste 😅 Era el {secreto}")