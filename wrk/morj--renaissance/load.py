#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
import platform
print(platform.python_version())
print("--------------------------------\n")

from textwrap import wrap
import os
import keras_cv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf
import tensorflow.experimental.numpy as tnp
from keras_cv.models.stable_diffusion.clip_tokenizer import SimpleTokenizer
from keras_cv.models.stable_diffusion.diffusion_model import DiffusionModel
from keras_cv.models.stable_diffusion.image_encoder import ImageEncoder
from keras_cv.models.stable_diffusion.noise_scheduler import NoiseScheduler
from keras_cv.models.stable_diffusion.text_encoder import TextEncoder
from tensorflow import keras

# 3. Create a base Stable diffusion Model
my_base_model = keras_cv.models.StableDiffusion(img_width=512, img_height=512)

# 4. Load Weights from the h5 model which is hosted on Hugging Face:
my_base_model.diffusion_model.load_weights('path/to/file/renaissance_model.h5')

# 5. Create a variable to hold the values of the to-be-generated image such as prompt, batch size, iterations, and seed
img = my_base_model.text_to_image(
       prompt='A woman with an enigmatic smile against a dark background',
       batch_size=1,  # How many images to generate at once
       num_steps=25,  # Number of iterations (controls image quality)
       seed=123,  # Set this to always get the same image from the same prompt
    )

# 6. Display the image using the function:
def plot_images(images):
    plt.figure(figsize=(5, 5))
    plt.imshow(images)
    plt.axis('off')
    
plot_images(img)
