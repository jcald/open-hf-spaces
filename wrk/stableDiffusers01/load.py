#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
import platform
print(platform.python_version())
print("--------------------------------\n")

from diffusers import StableDiffusionControlNetPipeline, ControlNetModel
import torch
from PIL import Image

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



# Cargar la imagen segmentada
image_path = "/home/nuevo/wrk/images/frames_00/frame_01_01_0.png"
segmented_image = Image.open(image_path).convert("RGB")
# Generar la imagen fotorealista desde la segmentación
generated_image = pipe(prompt="", image=segmented_image).images[0]

# Guardar la imagen generada
generated_image.save("generated_image.png")

