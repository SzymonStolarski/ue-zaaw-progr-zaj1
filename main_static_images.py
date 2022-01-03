import os

import cv2

from components.image_preprocessing.image_preprocessor import ImagePreprocessor
from components.predictor.predictor import Predictor


FOLDER_PATH = 'input_images'
MIN_SCORE = 0.2
FILTER_PREDICTIONS = ['person']

img_preprocessor = ImagePreprocessor()
predictor = Predictor('efficientdet_lite2')
predictor.load_model()

dict_with_results = {}

iterator = 1
for filename in os.listdir(FOLDER_PATH):
    print(filename)
    rgb_img, rgb_tensor = img_preprocessor.read_transform(
                            f'{FOLDER_PATH}/{filename}')
    predictor.predict(rgb_tensor)
    img_with_boxes = predictor.draw_boxes(rgb_img, min_score=MIN_SCORE,
                                          filter_predictions=FILTER_PREDICTIONS
                                          )
    dict_with_results[f'img{iterator}_predicted'] = img_with_boxes
    iterator += 1
print('done!')

# Show an example image with predictions
cv2.imshow('image', dict_with_results['img3_predicted'])
cv2.waitKey(0)
cv2.destroyAllWindows()
