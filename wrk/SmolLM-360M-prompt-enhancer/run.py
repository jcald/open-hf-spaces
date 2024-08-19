#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
import platform
import argparse
from transformers import pipeline

# Imprimir versión de Python
print(platform.python_version())
print("--------------------------------\n")

# Configurar argparse para recibir el argumento del prompt
parser = argparse.ArgumentParser(description="Text generation using SmolLM model.")
parser.add_argument('prompt', type=str, help="The prompt to use for text generation.")
args = parser.parse_args()

# Inicializar la pipeline de generación de texto
pipe = pipeline("text-generation", model="kadirnar/SmolLM-360M-prompt-enhancer")

# Generar texto usando el prompt proporcionado
result = pipe(args.prompt)

# Imprimir el resultado
print(result)

