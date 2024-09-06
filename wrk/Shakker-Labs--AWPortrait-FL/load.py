#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
import platform
print(platform.python_version())
print("--------------------------------\n")

import torch
from diffusers import FluxPipeline

pipe = FluxPipeline.from_pretrained("Shakker-Labs/AWPortrait-FL", torch_dtype=torch.bfloat16)
pipe.to("cuda")

prompt = "close up portrait, Amidst the interplay of light and shadows in a photography studio,a soft spotlight traces the contours of a face,highlighting a figure clad in a sleek black turtleneck. The garment,hugging the skin with subtle luxury,complements the Caucasian model's understated makeup,embodying minimalist elegance. Behind,a pale gray backdrop extends,its fine texture shimmering subtly in the dim light,artfully balancing the composition and focusing attention on the subject. In a palette of black,gray,and skin tones,simplicity intertwines with profundity,as every detail whispers untold stories."

image = pipe(prompt, 
             num_inference_steps=24, 
             guidance_scale=3.5,
             width=768, height=1024,
            ).images[0]
image.save(f"example.png")

