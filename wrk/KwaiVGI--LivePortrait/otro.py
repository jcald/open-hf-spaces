#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
import platform
print(platform.python_version())
print("--------------------------------\n")

import torch
import os.path as osp
import cv2
import tyro
from src.utils.helper import load_description
from src.gradio_pipeline import GradioPipeline
from src.config.crop_config import CropConfig
from src.config.argument_config import ArgumentConfig
from src.config.inference_config import InferenceConfig

# Definir las configuraciones
def partial_fields(target_class, kwargs):
    return target_class(**{k: v for k, v in kwargs.items() if hasattr(target_class, k)})

# Configuración de CLI con Tyro
tyro.extras.set_accent_color("bright_cyan")
args = tyro.cli(ArgumentConfig)

# Especificar configuraciones para inferencia
inference_cfg = partial_fields(InferenceConfig, args.__dict__)
crop_cfg = partial_fields(CropConfig, args.__dict__)

# Inicializar la pipeline
gradio_pipeline = GradioPipeline(
    inference_cfg=inference_cfg,
    crop_cfg=crop_cfg,
    args=args
)

# Verificar si el video tiene proporciones cuadradas
def is_square_video(video_path):
    video = cv2.VideoCapture(video_path)
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    video.release()

    if width != height:
        raise ValueError("Error: el video no tiene una relación de aspecto cuadrada. Actualmente solo se admiten videos cuadrados.")
    print("El video tiene una proporción cuadrada.")
    return True

def execute_video(image_input, video_input, flag_relative, flag_do_crop, flag_remap):
    # Llamada para procesar el video
    return gradio_pipeline.execute_video(image_input, video_input, flag_relative, flag_do_crop, flag_remap)

def execute_image(eye_ratio, lip_ratio, image_input, flag_do_crop):
    # Llamada para procesar la imagen
    return gradio_pipeline.execute_image(eye_ratio, lip_ratio, image_input, flag_do_crop)

def main():
    # Obtener entradas desde la consola o archivos
    print("Introduce la ruta de la imagen de entrada:")
    image_input = input().strip()

    print("Introduce la ruta del video de entrada:")
    video_input = input().strip()

    # Verificar si el video es cuadrado
    is_square_video(video_input)

    # Opciones de procesamiento
    print("¿Activar movimiento relativo? (True/False):")
    flag_relative = input().strip().lower() == 'true'

    print("¿Hacer crop de la imagen? (True/False):")
    flag_do_crop = input().strip().lower() == 'true'

    print("¿Habilitar remapeo (paste-back)? (True/False):")
    flag_remap = input().strip().lower() == 'true'

    # Ejecutar el pipeline de video
    output_video_path, output_video_concat_path = execute_video(image_input, video_input, flag_relative, flag_do_crop, flag_remap)

    print(f"Video generado en: {output_video_path}")
    print(f"Video concatenado generado en: {output_video_concat_path}")

if __name__ == "__main__":
    main()

