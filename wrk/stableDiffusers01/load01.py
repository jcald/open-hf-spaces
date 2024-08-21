#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
import platform
print(platform.python_version())
print("--------------------------------\n")

from diffusers import StableDiffusionControlNetPipeline, ControlNetModel
import torch
from PIL import Image
import re

# Cargar el modelo base de Stable Diffusion y el modelo de ControlNet entrenado para segmentación
model_id = "runwayml/stable-diffusion-v1-5"
controlnet = ControlNetModel.from_pretrained("lllyasviel/sd-controlnet-seg", torch_dtype=torch.float16)

# Usar un pipeline para procesamiento de imágenes
pipe = StableDiffusionControlNetPipeline.from_pretrained(model_id, controlnet=controlnet, torch_dtype=torch.float16)
pipe.to("cuda")
from diffusers import StableDiffusionControlNetPipeline, ControlNetModel
import torch

# Cargar el modelo base de Stable Diffusion y el modelo de ControlNet entrenado para segmentación
# model_id = "runwayml/stable-diffusion-v1-5"
# controlnet = ControlNetModel.from_pretrained("lllyasviel/sd-controlnet-seg", torch_dtype=torch.float16)
#
# # Usar un pipeline para procesamiento de imágenes
# pipe = StableDiffusionControlNetPipeline.from_pretrained(model_id, controlnet=controlnet, torch_dtype=torch.float16)
# pipe.to("cuda")


pattern = r'_0\.png$'
# Cargar la imagen segmentada
image_path = "/home/studio-lab-user/jcald/images/frame_01_04_0.png"
segmented_image = Image.open(image_path).convert("RGB")
# Generar la imagen fotorealista desde la segmentacion
generated_image = pipe(prompt="", image=segmented_image).images[0]
new_name = re.sub(pattern, '_1.png', image_path)
# Guardar la imagen generada
generated_image.save(new_name)

