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
    while True:
        registro = input("Ingrese un registro (o 'end' para salir): ")
        if registro.lower() == 'end':
            break

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

if __name__ == "__main__":
    main()
