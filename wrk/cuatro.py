#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
import platform
print(platform.python_version())
print("--------------------------------\n")

import subprocess
import os

# Obtener la versión actual de Conda
result = subprocess.run(["conda", "--version"], capture_output=True, text=True)
current_version = result.stdout.strip().split()[-1]

# Definir la versión objetivo
target_version = "24.7.1"

# Comparar las versiones
comparison = min([current_version, target_version], key=lambda v: list(map(int, v.split('.'))))

# Imprimir el valor de la comparación
print(f"Valor de la comparación: {comparison}")

# Guardar la comparación en un archivo
with open("solo.txt", "w") as file:
    file.write(comparison)

# Verificar si se requiere la actualización de Conda
if comparison > target_version:
    print("Actualizando Conda...............")
    # subprocess.run(["conda", "update", "-n", "base", "conda", "-y"])
else:
    print("La versión actual de Conda es menor o igual de 24.7.1. No es necesario actualizar.")

