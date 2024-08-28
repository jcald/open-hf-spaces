#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: set fileencoding=utf-8 :

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
import platform
print(platform.python_version())
print("--------------------------------\n")

# pip install --upgrade diffusers transformers scipy

import torch
from diffusers import StableDiffusionPipeline

model_id = "CompVis/stable-diffusion-v1-4"
device = "cuda"


pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to(device)

prompt = "a photo of an astronaut riding a horse on mars"
prompt = "Happy elephant running across the desert. 4K, --ar 3:2 --quality 2"
image = pipe(prompt).images[0]  
    
image.save("astronaut_rides_horse.png")

