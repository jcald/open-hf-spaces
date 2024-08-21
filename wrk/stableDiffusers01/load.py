#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
import platform
import os
import re
from diffusers import StableDiffusionControlNetPipeline, ControlNetModel
import torch
from PIL import Image

print(platform.python_version())
print("--------------------------------\n")

# Cargar el modelo base de Stable Diffusion y el modelo de ControlNet entrenado para segmentación
model_id = "runwayml/stable-diffusion-v1-5"
controlnet = ControlNetModel.from_pretrained("lllyasviel/sd-controlnet-seg", torch_dtype=torch.float16)

# Usar un pipeline para procesamiento de imágenes
pipe = StableDiffusionControlNetPipeline.from_pretrained(model_id, controlnet=controlnet, torch_dtype=torch.float16)
pipe.to("cuda")

# Definir el directorio a recorrer y el patrón de archivo a buscar
directory = "/home/studio-lab-user/jcald/ima/"
pattern = r'_0\.png$'

# Definir el prompt y el prompt negativo
prompt = "Create an image of a DJ performing on stage with vibrant neon lights and a futuristic atmosphere. The DJ is wearing sunglasses and a hoodie, focused on the turntables. Superimpose a semi-transparent overlay of a simplified, abstract human figure represented by colored lines and dots (as seen in a motion capture or skeletal tracking system) in the center of the image. The skeletal figure should have a dynamic pose, as if dancing to the music, and the colored lines should range across the spectrum, from red to violet."
negative_prompt = "blurry, low-quality, distorted"

# Recorrer el directorio y procesar las imágenes que coincidan con el patrón
for filename in os.listdir(directory):
    if re.search(pattern, filename):
        # Ruta completa de la imagen
        image_path = os.path.join(directory, filename)
        
        # Cargar la imagen segmentada
        segmented_image = Image.open(image_path).convert("RGB")
        
        # Generar la imagen fotorealista desde la segmentación
        generated_image = pipe(prompt=prompt, image=segmented_image, negative_prompt=negative_prompt).images[0]
        
        # Modificar el nombre del archivo
        new_name = re.sub(pattern, '_1.png', image_path)
        
        # Guardar la imagen generada
        generated_image.save(new_name)
        print(f"Imagen guardada: {new_name}")
