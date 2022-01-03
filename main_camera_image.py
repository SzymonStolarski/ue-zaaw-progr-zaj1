import cv2

from components.image_preprocessing.image_preprocessor import ImagePreprocessor
from components.predictor.predictor import Predictor


MIN_SCORE = 0.2
FILTER_PREDICTIONS = ['person']

img_preprocessor = ImagePreprocessor()
predictor = Predictor('efficientdet_lite2')
predictor.load_model()

cap = cv2.VideoCapture(0)
while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()

    rgb_img, rgb_tensor = img_preprocessor.transform(frame)
    predictor.predict(rgb_tensor)
    img_with_boxes = predictor.draw_boxes(rgb_img, min_score=MIN_SCORE,
                                          filter_predictions=FILTER_PREDICTIONS
                                          )

    cv2.imshow('camera image', img_with_boxes)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
