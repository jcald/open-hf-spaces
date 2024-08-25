#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
import platform
print(platform.python_version())
print("--------------------------------\n")

from gradio_client import Client

client = Client("multimodalart/flux-lora-the-explorer",
    hf_token="tu_api_key_aqui")
result = client.predict(
		prompt="Hello!!",
		cfg_scale=3.5,
		steps=28,
		randomize_seed=True,
		seed=2433143866,
		width=1024,
		height=1024,
		lora_scale=0.95,
		api_name="/run_lora"
)
print(result)
