#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: set fileencoding=utf-8 :

import requests
from PIL import Image

conversation = [
    {
      "role": "user",
      "content": [
          {"type": "text", "text": "What are these?"},
          {"type": "image"},
        ],
    },
]
prompt = processor.apply_chat_template(conversation, add_generation_prompt=True)

image_file = "http://images.cocodataset.org/val2017/000000039769.jpg"
raw_image = Image.open(requests.get(image_file, stream=True).raw)
inputs_image = processor(text=prompt, images=raw_image, return_tensors='pt').to(0, torch.float16)

output = model.generate(**inputs_video, max_new_tokens=100, do_sample=False)
print(processor.decode(output[0][2:], skip_special_tokens=True))

