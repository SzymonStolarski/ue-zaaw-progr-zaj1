import cv2

from components.image_preprocessing.image_preprocessor import ImagePreprocessor
from components.predictor.predictor import Predictor


FILE_PATH = 'input_images/img1.png'

img_preprocessor = ImagePreprocessor()
predictor = Predictor('efficientdet_lite2')

rgb_image, rgb_tensor = img_preprocessor.transform(FILE_PATH)

predictor.load_model()
predictor.predict(rgb_tensor)

image_with_boxes = predictor.draw_boxes(rgb_image, min_score=0.2,
                                        filter_predictions=['person'])


cv2.imshow('image', image_with_boxes)
cv2.waitKey(0)
cv2.destroyAllWindows()
