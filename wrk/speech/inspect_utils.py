#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
import platform
print(platform.python_version())
print("--------------------------------\n")

from transformers import pipeline

# Crear un pipeline para la tarea deseada
pipe = pipeline("automatic-speech-recognition", model="facebook/wav2vec2-base-960h")

# Verificar el modelo que se ha cargado
print(pipe.model.config.name_or_path)

