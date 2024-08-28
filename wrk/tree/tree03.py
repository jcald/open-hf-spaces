#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
import platform
print(platform.python_version())
print("--------------------------------\n")

def proceso(registro):
    # Aquí va la lógica específica del proceso
    print("Procesando registro:", registro)
    # ...

repeticiones = 5  # Valor predeterminado

with open('registros.txt', 'r') as archivo:
    while True:
        registro = archivo.readline().strip()
        if not registro:
            break

        print("Nuevo registro:", registro)
        repetir = input("Repetir (s/n)? ")
        if repetir.lower() == 's':
            num_repeticiones = int(input("Número de repeticiones (Enter para {}): ".format(repeticiones)) or repeticiones)
            for _ in range(num_repeticiones):
                proceso(registro)
        else:
            proceso(registro)

        continuar = input("Continuar (s/n)? ")
        if continuar.lower() != 's':
            break
