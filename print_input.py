from imcCalculator import calculator_imc

'''edad = input("Pon tu edad:")

if edad >="18":
    print("Puedes pasar")
else:
    print("No puedes")

JUBILACION = 67
nombre= input("Introduce tu nombre: ")
anoNacimiento = int(input("Introduce tu año de nacimiento: "))
anoActual = int(input("Intruduce el año actual: "))
diferencia = anoActual-anoNacimiento

if diferencia <= JUBILACION:
    print(nombre, "Aun te quedan", JUBILACION-diferencia, "años para jubilarte, amigo ")
else:
    print("Disfruta de la vida!",nombre)'''


name = input("Introduce tu nombre: ")
weight = round(float(input("Introduce tu año de peso en 'Kilogramos': ")))
height = round(float(input("Introduce tu año de estatura en 'Metros': ")))

IMC = calculator_imc(weight, height)

if IMC <25:
    print(f"{name}, tu IMC es de {IMC}. Tienes peso normal")
elif IMC >= 25 and IMC < 30:
    print(f"{name}, tu IMC es de {IMC}. Tienes sobrepeso")
else:
    print(f"{name}, tu IMC es de {IMC}. Tienes obesidad")




