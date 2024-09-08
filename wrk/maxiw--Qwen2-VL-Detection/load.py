#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
import platform
print(platform.python_version())
print("--------------------------------\n")

import os
import re
import torch
import base64
from PIL import Image, ImageDraw
from io import BytesIO
from transformers import Qwen2VLForConditionalGeneration, AutoProcessor
from qwen_vl_utils import process_vision_info

# Cargar los modelos y procesadores
models = {
    "Qwen/Qwen2-VL-7B-Instruct": Qwen2VLForConditionalGeneration.from_pretrained("Qwen/Qwen2-VL-7B-Instruct", torch_dtype="auto", device_map="auto"),
    "Qwen/Qwen2-VL-2B-Instruct": Qwen2VLForConditionalGeneration.from_pretrained("Qwen/Qwen2-VL-2B-Instruct", torch_dtype="auto", device_map="auto")
}

processors = {
    "Qwen/Qwen2-VL-7B-Instruct": AutoProcessor.from_pretrained("Qwen/Qwen2-VL-7B-Instruct"),
    "Qwen/Qwen2-VL-2B-Instruct": AutoProcessor.from_pretrained("Qwen/Qwen2-VL-2B-Instruct")
}

# Convertir imagen a base64
def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str

# Dibujar cuadros delimitadores en la imagen
def draw_bounding_boxes(image, bounding_boxes, outline_color="red", line_width=2):
    draw = ImageDraw.Draw(image)
    for box in bounding_boxes:
        xmin, ymin, xmax, ymax = box
        draw.rectangle([xmin, ymin, xmax, ymax], outline=outline_color, width=line_width)
    return image

# Reescalar los cuadros delimitadores a las dimensiones originales de la imagen
def rescale_bounding_boxes(bounding_boxes, original_width, original_height, scaled_width=1000, scaled_height=1000):
    x_scale = original_width / scaled_width
    y_scale = original_height / scaled_height
    rescaled_boxes = []
    for box in bounding_boxes:
        xmin, ymin, xmax, ymax = box
        rescaled_box = [xmin * x_scale, ymin * y_scale, xmax * x_scale, ymax * y_scale]
        rescaled_boxes.append(rescaled_box)
    return rescaled_boxes

# Ejecutar el ejemplo con inputs desde archivos
def run_example(image_path, text_input, system_prompt, model_id="Qwen/Qwen2-VL-7B-Instruct", output_dir="out"):
    image = Image.open(image_path)
    model = models[model_id].eval()
    processor = processors[model_id]

    # Crear los mensajes para el modelo
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "image", "image": f"data:image;base64,{image_to_base64(image)}"},
                {"type": "text", "text": system_prompt},
                {"type": "text", "text": text_input},
            ],
        }
    ]

    # Procesar la entrada
    text = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    image_inputs, video_inputs = process_vision_info(messages)
    inputs = processor(text=[text], images=image_inputs, videos=video_inputs, padding=True, return_tensors="pt")
    inputs = inputs.to("cuda")

    # Generar salida del modelo
    generated_ids = model.generate(**inputs, max_new_tokens=128)
    generated_ids_trimmed = [out_ids[len(in_ids):] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)]
    output_text = processor.batch_decode(generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False)

    # Extraer cuadros delimitadores del texto de salida
    pattern = r'\[\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\]'
    matches = re.findall(pattern, str(output_text))
    parsed_boxes = [[int(num) for num in match] for match in matches]
    scaled_boxes = rescale_bounding_boxes(parsed_boxes, image.width, image.height)

    # Dibujar los cuadros en la imagen
    annotated_image = draw_bounding_boxes(image.copy(), scaled_boxes)

    # Guardar el resultado en el directorio de salida
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Guardar la imagen anotada
    image_filename = os.path.join(output_dir, f"annotated_{os.path.basename(image_path)}")
    annotated_image.save(image_filename)
    
    # Guardar el texto de salida
    text_filename = os.path.join(output_dir, f"output_{os.path.basename(image_path)}.txt")
    with open(text_filename, "w") as f:
        f.write(str(output_text))
    
    print(f"Result saved: {image_filename}, Text output: {text_filename}")

# Función para procesar archivos de entrada desde una carpeta
def process_input_folder(input_folder="inp", output_folder="out", system_prompt="You are a helpful assistant..."):
    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(input_folder, filename)
            text_input_file = os.path.splitext(filename)[0] + ".txt"
            text_input_path = os.path.join(input_folder, text_input_file)

            if os.path.exists(text_input_path):
                with open(text_input_path, "r") as f:
                    text_input = f.read()
                print(f"Processing {filename} with prompt: {text_input}")
                run_example(image_path, text_input, system_prompt, output_dir=output_folder)
            else:
                print(f"No text input found for {filename}")

# Ejecución
process_input_folder()

