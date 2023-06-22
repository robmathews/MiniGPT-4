import torch
import torchvision

print("PyTorch Version: ",torch.__version__)
print("Torchvision Version: ",torchvision.__version__)

if torch.cuda.is_available():
    print("if torch.cuda.is_available() returns TRUE")
else:
    print("if torch.cuda.is_available() returns FALSE")