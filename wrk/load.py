#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
import platform
print(platform.python_version())
print("--------------------------------\n")

# pip install --upgrade diffusers transformers scipy

import random
import string

def camelCase(texto_largo):
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

import torch
from diffusers import StableDiffusionPipeline

model_id = "CompVis/stable-diffusion-v1-4"
device = "cuda"


pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to(device)

# prompt = "a photo of an astronaut riding a horse on mars"
# prompt = "Happy elephant running across the desert. 4K, --ar 3:2 --quality 2"
# image = pipe(prompt).images[0]  
# image.save("astronaut_rides_horse.png")


#repeticiones = 1  # Valor predeterminado
# Obtener parámetros del usuario
num_images = 5
guidance_scale = 7.5
#seed_default = None
with open('prompts.txt', 'r') as archivo:
    while True:
        prompt = archivo.readline().strip()
        if not prompt:
            break

        print("Nuevo prompt:", prompt)
        images = pipe(prompt,
        num_inference_steps=50,
        guidance_scale=guidance_scale,
        num_images=num_images,
        ).images


        largo=len(images) 
        print(largo)
        #repetir = input("Repetir (s/n)? ")
        repetir="s"
        if repetir.lower() == 's':
            num_repeticiones = largo 	#int(input("Número de repeticiones (Enter para {}): ".format(repeticiones)) or repeticiones)
            for i in range(num_repeticiones):
                #proceso(prompt)
                name=camelCase(prompt) + f"{i:02d}.png"
                print(name)
                images[i].save(name)
        else:
            #proceso(prompt)
            i=0
            name=camelCase(prompt) + f"{i:02d}.png"
#            image = pipe(prompt).images[i]
            images[i].save(name)

        #continuar = input("Continuar (s/n)? ")
        #if continuar.lower() != 's':
        #    break





#def proceso(prompt):
#    # Aquí va la lógica específica del proceso
#    print("Procesando prompt:", prompt)
#    # ...
