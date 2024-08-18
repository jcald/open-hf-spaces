#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
import platform
print(platform.python_version())
print("--------------------------------\n")

from PIL import Image

# Cargar la imagen segmentada
image_path = "/home/nuevo/wrk/images/frames_00/frame_01_01_0.png"
segmented_image = Image.open(image_path).convert("RGB")
# Generar la imagen fotorealista desde la segmentación
generated_image = pipe(prompt="", image=segmented_image).images[0]

# Guardar la imagen generada
generated_image.save("generated_image.png")

