from PIL import Image
from torchvision import transforms

TARGET_SIZE = (224, 224)

transform = transforms.Compose([
    transforms.Resize(TARGET_SIZE),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])


def preprocess(file):
    image = Image.open(file).convert("RGB")

    original_size = image.size

    tensor = transform(image)

    tensor = tensor.unsqueeze(0)

    return {
        "tensor": tensor,
        "original_size": original_size,
        "processed_size": tensor.shape
    }