#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
import platform
print(platform.python_version())
print("--------------------------------\n")

import os
import torch
from colpali_engine.models.paligemma_colbert_architecture import ColPali
from colpali_engine.trainer.retrieval_evaluator import CustomEvaluator
from colpali_engine.utils.colpali_processing_utils import (
    process_images,
    process_queries,
)
from pdf2image import convert_from_path
from PIL import Image
from torch.utils.data import DataLoader
from tqdm import tqdm
from transformers import Qwen2VLForConditionalGeneration, AutoTokenizer, AutoProcessor
from qwen_vl_utils import process_vision_info

def model_inference(images, text):
    images = [{"type": "image", "image": Image.open(image)} for image in images]
    images.append({"type": "text", "text": text})

    model = Qwen2VLForConditionalGeneration.from_pretrained(
        "Qwen/Qwen2-VL-2B-Instruct",
        trust_remote_code=True,
        torch_dtype=torch.bfloat16
    ).to("cuda:0")

    min_pixels = 256 * 28 * 28
    max_pixels = 1280 * 28 * 28
    processor = AutoProcessor.from_pretrained("Qwen/Qwen2-VL-2B-Instruct", min_pixels=min_pixels, max_pixels=max_pixels)

    messages = [{"role": "user", "content": images}]
    text = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    image_inputs, video_inputs = process_vision_info(messages)

    inputs = processor(
        text=[text],
        images=image_inputs,
        videos=video_inputs,
        padding=True,
        return_tensors="pt",
    )
    inputs = inputs.to("cuda")

    generated_ids = model.generate(**inputs, max_new_tokens=512)
    generated_ids_trimmed = [
        out_ids[len(in_ids):] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
    ]
    output_text = processor.batch_decode(
        generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
    )

    del model
    del processor
    torch.cuda.empty_cache()
    return output_text[0]


def process_input_output():
    input_dir = "inp/"
    output_dir = "out/"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Itera sobre los archivos en la carpeta de input
    for file in os.listdir(input_dir):
        if file.endswith(".txt"):
            with open(os.path.join(input_dir, file), 'r') as f:
                lines = f.readlines()
                text = lines[-1]  # Asume que el último renglón es el texto
                image_paths = [line.strip() for line in lines[:-1]]  # Imágenes en las líneas anteriores

            output_text = model_inference(image_paths, text)

            output_file = os.path.join(output_dir, f"output_{file}")
            with open(output_file, 'w') as f_out:
                f_out.write(output_text)
            print(f"Resultado guardado en: {output_file}")


if __name__ == "__main__":
    process_input_output()

