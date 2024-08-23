#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
import platform
print(platform.python_version())
print("--------------------------------\n")

from transformers import AutoModelForCTC

# Cargar el modelo
model = AutoModelForCTC.from_pretrained("facebook/wav2vec2-base-960h")

# Imprimir detalles del modelo
print(model.config)

