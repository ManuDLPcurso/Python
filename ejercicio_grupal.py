from functions import multiplicacion_enteros
from functions import suma_enteros
from functions import calcular_area_circunferencia
from functions import calcular_area_rectangulo

radio = float(input("Ingrese el radio de la circunferencia: "))
base = float(input("Introduce la base del rectángulo: "))
altura = float(input("Introduce la altura del rectángulo: "))
numero_1 = int(input("Ingrese primer numero: "))
numero_2 = int(input("Ingrese un numero entero: "))


multiplicacion = multiplicacion_enteros(numero_1, numero_2)
suma = suma_enteros(numero_1, numero_2)
areaCircunferencia = calcular_area_circunferencia(radio)
areaRectangulo = calcular_area_rectangulo(base, altura)

print(
    f"-- Multiplicacion: {multiplicacion} \n-- Suma: {suma} \n-- Area de la circunferencia: {areaCircunferencia} \n-- Area del rectangulo: {areaRectangulo}"
)
