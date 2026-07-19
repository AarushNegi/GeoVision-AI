import torch
from torchvision.models import resnet50, ResNet50_Weights

# Load pretrained ResNet50
weights = ResNet50_Weights.DEFAULT
model = resnet50(weights=weights)

# Remove the final classification layer
model = torch.nn.Sequential(*list(model.children())[:-1])

# Inference mode
model.eval()