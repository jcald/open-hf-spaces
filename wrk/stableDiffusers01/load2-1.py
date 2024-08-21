#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
import platform
print(platform.python_version())
print("--------------------------------\n")


import torch
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler

model_id = "stabilityai/stable-diffusion-2-1"

# Use the DPMSolverMultistepScheduler (DPM-Solver++) scheduler here instead
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
pipe = pipe.to("cuda")

prompt = "back view,nude, sex, bubble buttom, as Atenea, era, demeter,afrodita , gorgeous, attractive, flirting, (((full body visible))), looking at viewer, portrait, photography, detailed skin, realistic, photo-realistic, 8k, highly detailed, full length frame, High detail RAW color art, sharp focus, hyperrealism"

image = pipe(prompt).images[0]
image.save("girk00.png")
image = pipe(prompt).images[0]
image.save("girk01.png")
