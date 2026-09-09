"""
Modulo con funciones que realizan calculos aritmeticos.
"""


def calcular_area_circunferencia(radio: float) -> float:
    """
    Calcula el area de una circunferencia

    Params:
    - radio= Radio de la circunferencia

    Return:
    - Area de la circunferencia
    """
    PI = 3.14
    area = PI * (radio * radio)

    return area


def multiplicacion_enteros(num1: int, num2: int) -> int:
    """
    Calcula la multiplicacion de dos numeros enteros

    Params:
    - num1:Es una entrada por teclado del usuario de un numero
    - num2:Es una entrada por teclado del usuario de un numero


    Return:
    - Devuelve la multiplicacion
    """
    resultado = num1 * num2
    return resultado


def suma_enteros(num1: int, num2: int) -> int:
    """
    Devuelve la suma de dos números enteros.

    params:
    - num1: Es una entrada del usuario de un numero
    - num2: Es una entrada del usuario de un numero
    """

    suma = num1 + num2

    return suma


def calcular_area_rectangulo(base: float, altura: float) -> float:
    """
    Devuelve el área de un rectángulo.

    params:
    - base: Es la longitud de la base del rectángulo
    - altura: Es la longitud de la altura del rectángulo
    """

    area = base * altura

    return area
