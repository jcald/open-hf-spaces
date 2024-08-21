#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
import platform
print(platform.python_version())
print("--------------------------------\n")

import platform
print(platform.python_version())
print("--------------------------------\n")

import torch
from diffusers import DiffusionPipeline, AutoencoderKL
from PIL import Image

# Cargar VAE (Variational Autoencoder)
vae = AutoencoderKL.from_pretrained("madebyollin/sdxl-vae-fp16-fix", torch_dtype=torch.float16)

# Cargar el pipeline base
pipe = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0", vae=vae, torch_dtype=torch.float16, variant="fp16", use_safetensors=True)
pipe.to("cuda")

# Cargar el refiner
refiner = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-refiner-1.0", vae=vae, torch_dtype=torch.float16, use_safetensors=True, variant="fp16")
refiner.to("cuda")

# Parámetros de la generación de imágenes
n_steps = 40
high_noise_frac = 0.7

# Definir el prompt
prompt = "A majestic lion jumping from a big stone at night"

# Generar la imagen utilizando el pipeline base
latent_image = pipe(prompt=prompt, num_inference_steps=n_steps, denoising_end=high_noise_frac, output_type="latent").images

# Refinar la imagen utilizando el refiner
final_image = refiner(prompt=prompt, num_inference_steps=n_steps, denoising_start=high_noise_frac, image=latent_image).images[0]

# Convertir la imagen generada a formato PIL para guardarla o mostrarla
final_image_pil = final_image.cpu().permute(1, 2, 0).numpy()
final_image_pil = (final_image_pil * 255).round().astype("uint8")
final_image_pil = Image.fromarray(final_image_pil)

# Guardar la imagen
final_image_pil.save("output_image.png")

# Mostrar la imagen
final_image_pil.show()

