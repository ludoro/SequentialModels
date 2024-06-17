import torch
import torch.nn as nn
from torch.nn import functional as F

# Set a seed.
torch.manual_seed(1412)

# Read the data
with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()













# Questions:

# 1. Add a Smoothing algorithm of your choice. Does that change perplexity on the test set?
# 2. Use a proper tokenizer. Does that change perplexity on the test set?
