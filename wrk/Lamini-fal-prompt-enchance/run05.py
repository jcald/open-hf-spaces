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

# Determinar si una GPU está disponible y establecer el dispositivo adecuado
device = 0 if torch.cuda.is_available() else -1

# Inicializar la pipeline de generación de texto en el dispositivo adecuado
#pipe = pipeline("text-generation", model="kadirnar/SmolLM-360M-prompt-enhancer", device=device)
pipe = pipeline("text2text-generation", model="gokaygokay/Lamini-fal-prompt-enchance", device=device)
# Abrir el archivo para guardar los prompts y las respuestas
with open("prompts_and_responses.txt", "a", encoding="utf-8") as f:
    while True:
        # Solicitar el prompt al usuario
        prompt = input("Introduce el prompt (o 'end' para terminar): ")
        
        if prompt.lower() == 'end':
            print("Finalizando...")
            break
        
        # Generar el texto a partir del prompt proporcionado
        result = pipe(prompt, max_new_tokens=500)  # , return_full_text=True)
        #result = pipe(prompt, max_length=500, max_new_tokens=500)  # , return_full_text=True)
        
        # Extraer el texto generado
        generated_text = result[0]['generated_text']
        
        # Imprimir y guardar el prompt y la respuesta en el archivo
        print(f"Respuesta generada: {generated_text}")
        f.write(f"Prompt: {prompt}\nRespuesta: {generated_text}\n\n")

print("Se han guardado los prompts y las respuestas.")

