import random

print("Piedra, papel o tijera, JAMG")

print("1 = piedra")
print("2 = papel")
print("3 = tijera")
    
tirada = input("escoge tu tirada: ")

tiradaordenador = random.randint(1,3)

if tiradaordenador == 1:
    print("El ordenador ha sacado piedra")
elif tiradaordenador == 2:
    print("El ordenador ha sacado papel")
elif tiradaordenador == 3:
    print("El ordenador ha sacado tijera")
