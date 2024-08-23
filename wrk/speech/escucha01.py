#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
import platform
print(platform.python_version())
print("--------------------------------\n")

import os
from transformers import pipeline
import torchaudio

# Directorio donde se encuentran los archivos de audio
input_dir = "input"

# Crear el pipeline de reconocimiento automático de voz (ASR)
pipe = pipeline("automatic-speech-recognition", model="facebook/wav2vec2-base-960h", device=0)

# Iterar sobre los archivos de audio en el directorio INPUT
for filename in os.listdir(input_dir):
    if filename.endswith(".wav"):  # Asegúrate de que solo se procesen archivos de audio .wav
        filepath = os.path.join(input_dir, filename)
        
        # Cargar el archivo de audio usando torchaudio
        audio, rate = torchaudio.load(filepath)
        
        # Convertir el tensor de audio a una lista de floats
        input_values = audio.squeeze().tolist()
        
        # Transcribir el archivo de audio
        result = pipe(input_values, sampling_rate=rate)
        
        # Mostrar el resultado
        print(f"Transcription for {filename}: {result['text']}")

