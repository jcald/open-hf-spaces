#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
import platform
import argparse
from transformers import pipeline
import torch

# Imprimir versión de Python
print(platform.python_version())
print("--------------------------------\n")

# Configurar argparse para recibir el argumento del prompt
parser = argparse.ArgumentParser(description="Text generation using SmolLM model.")
parser.add_argument('prompt', type=str, help="The prompt to use for text generation.")
args = parser.parse_args()

# Determinar si una GPU está disponible y establecer el dispositivo adecuado
device = 0 if torch.cuda.is_available() else -1

# Inicializar la pipeline de generación de texto en el dispositivo adecuado
pipe = pipeline("text-generation", model="kadirnar/SmolLM-360M-prompt-enhancer", device=device)

# Establecer parámetros para la generación por chunks (en este caso, el max_length)
max_length = 500
max_new_tokens = 100

# Generar texto por chunks usando un bucle
result = pipe(args.prompt, max_length=max_length, max_new_tokens=max_new_tokens, return_full_text=False)

# Procesar e imprimir cada chunk generado
for chunk in result:
    generated_text = chunk['generated_text']
    print(generated_text)

