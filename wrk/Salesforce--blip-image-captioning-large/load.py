#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
import platform
print(platform.python_version())
print("--------------------------------\n")

import torch
import requests
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large", torch_dtype=torch.float16).to("cuda")

img_url = 'https://storage.googleapis.com/sfr-vision-language-research/BLIP/demo.jpg' 
raw_image = Image.open(requests.get(img_url, stream=True).raw).convert('RGB')

# conditional image captioning
text = "a photography of"
inputs = processor(raw_image, text, return_tensors="pt").to("cuda", torch.float16)

out = model.generate(**inputs)
#print(processor.decode(out[0], skip_special_tokens=True))
#print(processor.decode(out[0], skip_special_tokens=True, clean_up_tokenization_spaces=True))
print(processor.decode(out[0], skip_special_tokens=True, clean_up_tokenization_spaces=False))
# >>> a photography of a woman and her dog

# unconditional image captioning
inputs = processor(raw_image, return_tensors="pt").to("cuda", torch.float16)

#out = model.generate(**inputs)
out = model.generate(**inputs, max_new_tokens=50)  # Ajusta el valor según sea necesario
print(processor.decode(out[0], skip_special_tokens=True))
#>>> a woman sitting on the beach with her dog

