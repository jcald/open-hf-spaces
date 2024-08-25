#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
import platform
print(platform.python_version())
print("--------------------------------\n")

import torch
from huggingface_hub import hf_hub_download
from torch import nn

# Generator Code

from huggingface_hub import hf_hub_download
from torch import nn
from torchvision.utils import save_image
class Generator(nn.Module):
    def __init__(self, ngpu=1, ngf=128, nz=128, nc =1):
        super(Generator, self).__init__()
        self.ngpu = ngpu
        self.main = nn.Sequential(
            nn.ConvTranspose2d(nz, ngf * 16, 4, 1, 0, bias=False),
            nn.BatchNorm2d(ngf*16),
            nn.LeakyReLU(0.2, inplace=True),
            nn.ConvTranspose2d(ngf*16, ngf*8, 4, 2, 1, bias=False),
            nn.BatchNorm2d(ngf * 8),
            nn.LeakyReLU(0.2, inplace=True),
            nn.ConvTranspose2d(ngf*8, ngf*4, 4, 2, 1, bias=False),
            nn.BatchNorm2d(ngf*4),
            nn.ReLU(True),
            nn.ConvTranspose2d(ngf*4, ngf*2, 4, 2, 1, bias=False),
            nn.BatchNorm2d(ngf * 2),
            nn.ReLU(True),
            nn.ConvTranspose2d(ngf*2,ngf, 4, 2, 1, bias=False),
            nn.BatchNorm2d(ngf),
            nn.ReLU(True),
            nn.ConvTranspose2d(ngf,nc, 4, 2, 1, bias=False),
            nn.Tanh()
        )
    def forward(self, input):
        return self.main(input)
model = Generator()
weights_path = hf_hub_download('oohtmeel/ct-gan-gen', 'lung_ct_generator_gan.pth')
model.load_state_dict(torch.load(weights_path, map_location=torch.device('cpu')))

out = model(torch.randn(128, 128, 1, 1))
save_image(out, "ct_scans.png", normalize=True)

