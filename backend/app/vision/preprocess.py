from PIL import Image
import numpy as np


TARGET_SIZE = (224, 224)


def load_image(file):
    image = Image.open(file)
    return image.convert("RGB")


def resize_image(image):
    return image.resize(TARGET_SIZE)


def normalize_image(image):
    image = np.array(image).astype(np.float32)
    image /= 255.0
    return image


def preprocess(file):
    image = load_image(file)

    original_size = image.size

    image = resize_image(image)

    processed = normalize_image(image)

    return {
        "image": processed,
        "original_size": original_size,
        "processed_size": processed.shape
    }