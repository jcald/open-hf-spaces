#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
import platform
print(platform.python_version())
print("--------------------------------\n")

def proceso(registro):
    # Aquí va la lógica de tu proceso
    print(f"Procesando registro: {registro}")
    # ... otras operaciones con el registro

def main():
    repeticiones = 0
    archivo = input("Ingrese el nombre del archivo: ")

    try:
        with open(archivo, 'r') as f:
            for linea in f:
                registro = linea.strip()

                while True:
                    try:
                        repeticiones = int(input("Ingrese el número de repeticiones (entero): "))
                        break
                    except ValueError:
                        print("Por favor, ingrese un número entero.")

                for _ in range(repeticiones):
                    proceso(registro)

                opcion = input("¿Repetir el registro? (sí/no): ")
                if opcion.lower() != 'sí':
                    break
    except FileNotFoundError:
        print(f"El archivo '{archivo}' no se encontró.")

if __name__ == "__main__":
    main()
