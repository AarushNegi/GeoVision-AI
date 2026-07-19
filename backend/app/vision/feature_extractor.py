import torch
from torchvision.models import resnet50, ResNet50_Weights

# Load pretrained weights
weights = ResNet50_Weights.DEFAULT

model = resnet50(weights=weights)

# Remove classification layer
model = torch.nn.Sequential(*list(model.children())[:-1])

model.eval()


def extract_features(image_tensor):
    with torch.no_grad():
        features = model(image_tensor)

    features = features.flatten()

    return features