# -*- coding: utf-8 -*-
"""actividad_01_enteros.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jIjFEEgAdfrINVKqeDLlppVx9Xn1h-T9
"""

print("Este es un script que retorna el cociente y residuo entre dos números")
a = float(input("ingrese un dividendo "))
b = float(input("ingrese el divisor "))
def div_mod(a,b):
    c = a / b
    r = a % b
    return print(f"el cociente es {c} y el residuo {r}")
div_mod(a,b)