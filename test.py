# -*- coding: utf-8 -*-
from steganogan import SteganoGAN
steganogan = SteganoGAN.load(architecture='basic')
steganogan.decode('research/output.png')