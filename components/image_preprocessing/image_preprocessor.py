import matplotlib.pyplot as plt
import cv2
import tensorflow as tf


class ImagePreprocessor:
    WIDTH = 1024
    HEIGHT = 1024

    def __init__(self) -> None:
        pass

    def transform(self, img_path):
        # Load image by Opencv2
        img = cv2.imread(img_path)
        # Resize to respect the input_shape
        img_resized = cv2.resize(img, (ImagePreprocessor.WIDTH,
                                 ImagePreprocessor.HEIGHT))

        # Convert img to RGB
        rgb_image = cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB)

        # Convert RGB image to tensor and expand dimensions
        rgb_tensor = tf.convert_to_tensor(rgb_image, dtype=tf.uint8)
        rgb_tensor = tf.expand_dims(rgb_tensor, 0)

        return rgb_image, rgb_tensor
