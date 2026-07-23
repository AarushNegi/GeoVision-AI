import torch
from torchvision.models import resnet50, ResNet50_Weights

weights = ResNet50_Weights.DEFAULT

model = resnet50(weights=weights)

# Remove the final classification layer
model = torch.nn.Sequential(*list(model.children())[:-1])

model.eval()


def extract_features(image_tensor):
    """
    Extract a 2048-dimensional feature vector from an image tensor.
    """

    with torch.no_grad():
        features = model(image_tensor)

    # Shape:
    # [1,2048,1,1]
    features = features.squeeze()

    return features