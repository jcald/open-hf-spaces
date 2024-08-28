#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
import platform
print(platform.python_version())
print("--------------------------------\n")

import random
import string

def camel_case_con_prefijo_aleatorio(texto_largo):
    """
    Convierte un texto largo a camelCase, coloca la palabra más significativa al inicio y
    añade un sufijo aleatorio de 4 caracteres al final.

    Args:
        texto_largo (str): El texto a convertir.

    Returns:
        str: El texto convertido a camelCase con prefijo y sufijo aleatorio.
    """

    # Convertimos el texto a minúsculas para facilitar el procesamiento
    texto_minusculas = texto_largo.lower()

    # Dividimos el texto en palabras
    palabras = texto_minusculas.split()

    # Identificamos la palabra más significativa (la primera por simplicidad)
    palabra_mas_significativa = palabras[0]

    # Convertimos el resto de las palabras a camelCase
    palabras_camel_case = [palabra.capitalize() for palabra in palabras[1:]]

    # Unimos todas las palabras en una sola cadena
    texto_camel_case = palabra_mas_significativa + "".join(palabras_camel_case)

    # Generamos un sufijo aleatorio de 4 caracteres
    caracteres = string.ascii_lowercase + string.digits
    sufijo_aleatorio = ''.join(random.choice(caracteres) for _ in range(4))

    # Combinamos el texto camelCase con el sufijo aleatorio
    resultado = texto_camel_case[0:20] + "_" + sufijo_aleatorio

    return resultado

# Ejemplo de uso:
texto_ejemplo = "esto es un texto muy largo para convertir a camel case"
resultado = camel_case_con_prefijo_aleatorio(texto_ejemplo)
print("12345678901234567890")
print(resultado)  # Por ejemplo: EstoEsUnTextoMuyLargoParaConvertirACamelCase3k8f
