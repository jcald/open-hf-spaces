#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :

import os
from gradio_client import Client

def main():
    # Crear el directorio de salida si no existe
    if not os.path.exists('salida'):
        os.makedirs('salida')
    
    client = Client("black-forest-labs/FLUX.1-dev")
    
    while True:
        # Solicitar el prompt al usuario
        prompt = input("Introduce el prompt (o 'end' para salir): ")
        
        if prompt.lower() == 'end':
            break
        
        result = client.predict(
            prompt=prompt,
            seed=0,
            randomize_seed=True,
            width=1024,
            height=1024,
            guidance_scale=3.5,
            num_inference_steps=28,
            api_name="/infer"
        )
        
        # Verificar el tipo de resultado
        print(f"Tipo de resultado: {type(result)}")
        print(f"Contenido del resultado: {result}")

        # Asumir que el primer elemento de la tupla es la ruta del archivo de imagen
        image_path = result[0]  # Ajusta esto según la estructura real del resultado
        
        # Leer la imagen desde la ruta proporcionada
        with open(image_path, 'rb') as f:
            image_bytes = f.read()
        
        # Guardar el resultado en el directorio de salida
        output_path = os.path.join('salida', f"{prompt[:10]}.webp")  # Usa los primeros 10 caracteres del prompt para el nombre del archivo
        with open(output_path, 'wb') as f:
            f.write(image_bytes)
        
        print(f"Imagen guardada en: {output_path}")

if __name__ == "__main__":
    main()

