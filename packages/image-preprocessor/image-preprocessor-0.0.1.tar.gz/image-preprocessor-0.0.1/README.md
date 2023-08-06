# Image Preprocessor

Simple image preprocessor I made while working on my first Keras binary classification convolutional neural network. Converts images from specified directories into NumPy arrays. Its functionality will be expanded out of necessity.

# Installation

Install through pip as shown:

```bash
pip install image-preprocessor
```

# Example usage

```py
from image_preprocessor import ImagePreprocessor

# Vehicle-label correlations
vehicle_types = {
    0 : 'boat',
    1 : 'car',
    2 : 'motorcycle',
    3 : 'plane'
}

# Create the ImagePreprocessor object
ip = ImagePreprocessor(
    pixels=64,
    normalization=255,
    training_threshold=0.7,
    resize_method='square resize',
    color_mode='L'
)

# Prepare the images in select directories
package = ip.preprocess_dirs(
    paths=['images/boat', 'images/car', 'images/motorcycle', 'images/plane'],
    labels=[0, 1, 2, 3],
    partition=True
)

# Go on and do your neural network stuff 
train_features = package['TRAIN_IMAGES']
train_labels = package['TRAIN_LABELS']
test_features = package['TEST_IMAGES']
test_labels = package['TEST_LABELS']
```