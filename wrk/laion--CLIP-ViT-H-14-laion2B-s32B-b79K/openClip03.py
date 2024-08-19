#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :

import platform
from PIL import Image
import matplotlib.pyplot as plt
import torch
import open_clip

# Ver la versión de Python
print(platform.python_version())
print("--------------------------------\n")

# Cargar el modelo y las transformaciones
model, preprocess_train, preprocess_val = open_clip.create_model_and_transforms('hf-hub:laion/CLIP-ViT-H-14-laion2B-s32B-b79K')
tokenizer = open_clip.get_tokenizer('hf-hub:laion/CLIP-ViT-H-14-laion2B-s32B-b79K')

# Texto de ejemplo
text_input = "A photo of a cat"
#text_input = "a photo of a cat's head"

# Imagen de ejemplo
#image_path = "gato02.jpg"
image_path = "gatoLat01.png"
image = Image.open(image_path)

# Mostrar la imagen original
plt.imshow(image)
plt.title("Imagen original")
plt.axis('off')
plt.show()

# Preprocesar la imagen
image_preprocessed = preprocess_val(image).unsqueeze(0)  # Añadir dimensión batch

# Tokenizar el texto
text_tokens = tokenizer([text_input])

# Mover el modelo y los datos a la CPU
device = "cpu"
model.to(device)
image_preprocessed = image_preprocessed.to(device)
text_tokens = text_tokens.to(device)

# Obtener las features (embeddings) sin gradiente
with torch.no_grad():
    image_features = model.encode_image(image_preprocessed)
    text_features = model.encode_text(text_tokens)

# Normalizar los embeddings
image_features /= image_features.norm(dim=-1, keepdim=True)
text_features /= text_features.norm(dim=-1, keepdim=True)

# Similaridad de coseno entre la imagen y el texto
similarity = (image_features @ text_features.T).item()

# Imprimir la similaridad calculada
print(f"Similaridad de coseno entre la imagen y el texto: {similarity}")

