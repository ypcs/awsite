#!/usr/bin/env python
# -*- coding: utf-8 -*-

# (c) 2012 Ville Korhonen <ville@xd.fi>

import sys
import os
from math import floor

MASK_CHAR = "X"     # Use this char to mask keys
MASK_SIZE = 0.65    # How large percentage of a key should be masked?

def mask_key(key, mask_size=MASK_SIZE):
    """Masks a key for output to logs etc"""
    mask_length = int(floor(len(key) * mask_size))
    masked_key = key[0:len(key) - mask_length] + mask_length * MASK_CHAR    
    return masked_key

