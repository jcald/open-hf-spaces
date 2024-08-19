#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
import platform
print(platform.python_version())
print("--------------------------------\n")

import open_clip
import torch
from PIL import Image

# Cargar el modelo y las transformaciones
model, preprocess_train, preprocess_val = open_clip.create_model_and_transforms('hf-hub:laion/CLIP-ViT-H-14-laion2B-s32B-b79K')
tokenizer = open_clip.get_tokenizer('hf-hub:laion/CLIP-ViT-H-14-laion2B-s32B-b79K')

# Texto de ejemplo
text_input = "A photo of a cat"

# Imagen de ejemplo
image_path = "gato02.jpg"
image = Image.open(image_path)

# Preprocesar la imagen
image_preprocessed = preprocess_val(image).unsqueeze(0)  # Añadir dimensión batch
# Disminuir el tamaño de la imagen (por ejemplo)
#image_preprocessed = preprocess_val(image.resize((224, 224))).unsqueeze(0)

# Tokenizar el texto
text_tokens = tokenizer([text_input])

# Mover a la misma device del modelo (si es necesario)
#device = "cuda" if torch.cuda.is_available() else "cpu"
#model.to(device)
device = "cpu"
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

