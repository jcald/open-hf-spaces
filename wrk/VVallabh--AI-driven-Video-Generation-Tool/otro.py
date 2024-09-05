#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
import platform
print(platform.python_version())
print("--------------------------------\n")

import torch
from diffusers import DiffusionPipeline, DPMSolverMultistepScheduler
from diffusers.utils import export_to_video
import imageio
import matplotlib.pyplot as plt

# Cargar el modelo
pipe = DiffusionPipeline.from_pretrained("damo-vilab/text-to-video-ms-1.7b", torch_dtype=torch.float16, variant="fp16")
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
pipe.enable_model_cpu_offload()
pipe.enable_vae_slicing()

def model(prompt, video_duration_seconds):
    # Número de frames según la duración del video
    num_frames = video_duration_seconds * 10
    
    # Generar los frames con el modelo
    video_frames = pipe(prompt, negative_prompt="low quality",
                        num_inference_steps=25, num_frames=num_frames).frames
    
    # Exportar los frames como video
    video_path = export_to_video(video_frames)
    
    # Mostrar una captura del primer frame
    first_frame = video_frames[0]
    plt.imshow(first_frame)
    plt.axis('off')
    plt.show()

    return video_path

def main():
    # Solicitar input al usuario
    prompt = input("Introduce el texto para generar el video: ")
    video_duration_seconds = int(input("Introduce la duración del video en segundos (1-10): "))
    
    # Llamar a la función del modelo
    output_video_path = model(prompt, video_duration_seconds)
    print(f"Video generado y guardado en: {output_video_path}")

if __name__ == "__main__":
    main()

