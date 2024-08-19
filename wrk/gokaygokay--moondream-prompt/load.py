#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
import platform
print(platform.python_version())
print("--------------------------------\n")

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from PIL import Image

DEVICE = "cuda"
DTYPE = torch.float32 if DEVICE == "cpu" else torch.float16 # CPU doesn't support float16
revision = "ac6c8fc0ba757c6c4d7d541fdd0e63618457350c"
tokenizer = AutoTokenizer.from_pretrained("gokaygokay/moondream-prompt", revision=revision)
moondream = AutoModelForCausalLM.from_pretrained("gokaygokay/moondream-prompt",trust_remote_code=True,
    torch_dtype=DTYPE, device_map={"": DEVICE}, revision=revision)
moondream.eval()

image_path = "gatoLat01.png"
image = Image.open(image_path).convert("RGB")
md_answer = moondream.answer_question(
        moondream.encode_image(image),
        "Describe this image and its style in a very detailed manner",
        tokenizer=tokenizer,
    )

print(md_answer)

