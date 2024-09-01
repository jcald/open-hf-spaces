#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: set fileencoding=utf-8 :

conversation_1 = [
    {
      "role": "user",
      "content": [
          {"type": "text", "text": "What's the content of the image>"},
          {"type": "image"},
        ],
    }
]
conversation_2 = [
    {
      "role": "user",
      "content": [
          {"type": "text", "text": "Why is this video funny?"},
          {"type": "video"},
        ],
    },
]
prompt_1 = processor.apply_chat_template(conversation_1, add_generation_prompt=True)
prompt_2 = processor.apply_chat_template(conversation_2, add_generation_prompt=True)

s = processor(text=[prompt_1, prompt_2], images=image, videos=clip, padding=True, return_tensors="pt").to(model.device)

# Generate
generate_ids = model.generate(**inputs, max_new_tokens=100)
out = processor.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)
print(out)

