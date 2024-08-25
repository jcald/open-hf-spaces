#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
import platform
print(platform.python_version())
print("--------------------------------\n")

from gradio_client import Client

client = Client("multimodalart/flux-lora-the-explorer")
result = client.predict(
		width=1024,
		height=1024,
		api_name="/update_selection"
)
print(result)

