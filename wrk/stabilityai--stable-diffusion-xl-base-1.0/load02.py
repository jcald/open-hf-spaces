#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
import platform
import os
import re
from diffusers import StableDiffusionXLPipeline
#from diffusers import StableDiffusionControlNetPipeline, ControlNetModel
import torch
from PIL import Image

print(platform.python_version())
print("--------------------------------\n")

model_path = "stabilityai/stable-diffusion-xl-base-1.0"
pipe = StableDiffusionXLPipeline.from_pretrained(model_path, torch_dtype=torch.float8)
pipe.to("cuda")
pipe.load_lora_weights("davizca87/c-a-g-coinmaker", weight_name="c01n-000010.safetensors")


# Definir el directorio a recorrer y el patrón de archivo a buscar
directory = "/home/studio-lab-user/jcald/images/"
pattern = r'_0\.png$'

# Definir el prompt y el prompt negativo
prompt = "A photorealistic image of a futuristic city skyline at sunset"
prompt = "c01n..."
negative_prompt = "blurry, low-quality, distorted"
lora_scale= 0.9

generated_image = pipe(prompt, num_inference_steps=30, guidance_scale=7.5, cross_attention_kwargs={"scale": lora_scale}).images[0]
image.save("image.png")
print(f"Imagen guardada: image.png")

