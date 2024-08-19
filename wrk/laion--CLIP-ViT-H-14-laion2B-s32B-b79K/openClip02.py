#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
import platform
import open_clip
import torch
from PIL import Image
import matplotlib.pyplot as plt

print(platform.python_version())
print("--------------------------------\n")

# Cargar el modelo y las transformaciones
model, preprocess_train, preprocess_val = open_clip.create_model_and_transforms('hf-hub:laion/CLIP-ViT-H-14-laion2B-s32B-b79K')
tokenizer = open_clip.get_tokenizer('hf-hub:laion/CLIP-ViT-H-14-laion2B-s32B-b79K')

# Texto de ejemplo
text_input = "A photo of a head cat"

# Imagen de ejemplo
image_path = "gato02.jpg"
image = Image.open(image_path)

# Mostrar la imagen antes de la comparación
plt.imshow(image)
plt.title("Imagen para la comparación: gato02.jpg")
plt.axis('off')  # Desactivar los ejes para una visualización más clara
plt.show()

# Preprocesar la imagen
image_preprocessed = preprocess_val(image).unsqueeze(0)  # Añadir dimensión batch

# Tokenizar el texto
text_tokens = tokenizer([text_input])

# Mover a la misma device del modelo (si es necesario)
device = "cpu"  # Se ejecuta en CPU para evitar problemas de memoria
model.to(device)

image_preprocessed = image_preprocessed.to(device)
text_tokens = text_tokens.to(device)

# Obtener las features (embeddings)
with torch.no_grad():
    image_features = model.encode_image(image_preprocessed)
    text_features = model.encode_text(text_tokens)

# Normalizar los embeddings si es necesario
image_features /= image_features.norm(dim=-1, keepdim=True)
text_features /= text_features.norm(dim=-1, keepdim=True)

# Similaridad de coseno entre la imagen y el texto
similarity = (image_features @ text_features.T).item()

print(f"Similaridad de coseno: {similarity}")

