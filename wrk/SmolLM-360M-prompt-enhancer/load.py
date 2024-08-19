#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
import platform
print(platform.python_version())
print("--------------------------------\n")

# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-generation", model="kadirnar/SmolLM-360M-prompt-enhancer")



# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("kadirnar/SmolLM-360M-prompt-enhancer")
model = AutoModelForCausalLM.from_pretrained("kadirnar/SmolLM-360M-prompt-enhancer")
