import cv2
import numpy as np
import tensorflow as tf


class ImagePreprocessor:
    """
    Class that prepares an image for TensorFlow object detection model
    prediction.
    """
    WIDTH = 512
    HEIGHT = 512

    def __init__(self) -> None:
        pass

    def read(self, img_path: str) -> np.ndarray:
        """
        Read an image with OpenCV.

        Parameters
        -----------
        img_path : str
            Path to image.
        """
        return cv2.imread(img_path)

    def transform(self, img: np.ndarray) -> tuple:
        """
        Perform OpenCV transofmations on a loaded image.

        Parameters
        -----------
        img : np.ndarray
            Loaded image to NumPy array.

        Returns
        -----------
        tuple
            Tuple containing:
                - transformed image in RGB,
                - RGB tensor of the transformed image.
        """
        # Resize to respect the input_shape
        img_resized = cv2.resize(img, (ImagePreprocessor.WIDTH,
                                 ImagePreprocessor.HEIGHT))

        # Convert img to RGB
        rgb_image = cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB)

        # Convert RGB image to tensor and expand dimensions
        rgb_tensor = tf.convert_to_tensor(rgb_image, dtype=tf.uint8)
        rgb_tensor = tf.expand_dims(rgb_tensor, 0)

        return rgb_image, rgb_tensor

    def read_transform(self, img_path: str) -> tuple:
        """
        Load an image and perform transformations on it.

        Parameters
        -----------
        img_path : str
            Path to image.

        Returns
        -----------
        tuple
            Tuple containing:
                - transformed image in RGB,
                - RGB tensor of the transformed image.
        """
        img = self.read(img_path)
        rgb_image, rgb_tensor = self.transform(img)

        return rgb_image, rgb_tensor
