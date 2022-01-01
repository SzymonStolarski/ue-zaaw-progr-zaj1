from time import time
import pandas as pd
import numpy as np
import tensorflow_hub as hub
import cv2

from components.exceptions.exceptions import *


MODEL_DICTIONARY = {
    'efficientdet_lite2': 'components/models/efficientdet_lite2_detection_1',
    'efficientdet_lite4': 'components/models/efficientdet_lite4_detection_2'}


class Predictor:
    """
    # TODO: add docstring
    """
    def __init__(self, model_name: str) -> None:
        self.__model_name = model_name
        # self.__min_score = min_score
        # self.__filter_predictions = filter_predictions
        self.__is_model_loaded = False
        self.__is_prediction_done = False

    def load_model(self):
        # Loading model - for this project's purpose storing models locally
        print(f'starting to load {self.__model_name} model...')
        self.model = hub.load(MODEL_DICTIONARY[self.__model_name])

        # Loading csv with labels of classes
        labels = pd.read_csv('components/models/image_labels.csv',
                             sep=';', index_col='ID')
        self.labels = labels['OBJECT (2017 REL.)']

        self.__is_model_loaded = True
        print(f'{self.__model_name} model loaded!')

    def predict(self, tensor):
        self.__check_is_model_loaded()
        # Creating prediction
        start_measuring_time = time()
        boxes, scores, classes, _ = self.model(tensor)
        self.__prediction_time = round(time() - start_measuring_time, 2)
        print(f'Prediction time: {self.__prediction_time} seconds')

        # Processing outputs - they will be stored in given instance
        # in order not to rerun the model every time we want to visualize
        # different results on the image
        predicted_labels = classes.numpy().astype('int')[0]
        self.__predicted_labels = np.array([self.labels[i]
                                            for i in predicted_labels])
        self.__predicted_boxes = boxes.numpy()[0].astype('int')
        self.__predicted_scores = scores.numpy()[0]

        self.__is_prediction_done = True

    def draw_boxes(self, img, min_score: float = 0.4,
                   filter_predictions: list[str] = None):
        self.__check_is_prediction_done()
        bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        img_boxes = bgr.copy()

        scores_to_visualize = self.__predicted_scores
        boxes_to_visualize = self.__predicted_boxes
        labels_to_visualize = self.__predicted_labels

        # Filtering if filter_predictions provided - drawing only
        # selected labels
        if filter_predictions is not None:
            # Select only those indexes that have selected labels provided
            # in filter_predictions
            idxes = [idx for idx, label in enumerate(self.__predicted_labels)
                     if label in filter_predictions]
            labels_to_visualize = np.array([self.__predicted_labels[i]
                                            for i in idxes])
            boxes_to_visualize = np.array([self.predicted_boxes[i]
                                           for i in idxes])
            scores_to_visualize = np.array([self.__predicted_scores[i]
                                            for i in idxes])

        # Putting the boxes and labels on the image
        for score, (ymin, xmin, ymax, xmax), label in zip(
                                                    scores_to_visualize,
                                                    boxes_to_visualize,
                                                    labels_to_visualize
                                                        ):
            # Filtering based on the min_score
            if score < min_score:
                continue

            score_txt = f'{100 * round(score,0)}'
            img_boxes = cv2.rectangle(img_boxes, (xmin, ymax), (xmax, ymin),
                                      (0, 255, 0), 1)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img_boxes, label, (xmin, ymax-10), font, 0.5,
                        (255, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(img_boxes, score_txt, (xmax, ymax-10), font, 0.5,
                        (255, 0, 0), 1, cv2.LINE_AA)

        return img_boxes

    def __check_is_model_loaded(self):
        if not self.__is_model_loaded:
            raise NotLoadedModelError(
                f"This instance of {self.__class__.__name__} has not "
                f"a loaded model yet; please call `load_model` first."
            )

    def __check_is_prediction_done(self):
        if not self.__is_prediction_done:
            raise PredictionsNotDoneError(
                f"This instance of {self.__class__.__name__} has not "
                f"yet made predictions with loaded model; "
                f"please call `predict` first."
            )

    @property
    def model_name(self) -> str:
        return self.__model_name

    @model_name.setter
    def model_name(self, value) -> None:
        self.__model_name = value

    @property
    def is_model_loaded(self) -> bool:
        return self.__is_model_loaded

    @property
    def is_prediction_done(self) -> bool:
        return self.__is_prediction_done

    @property
    def predicted_labels(self) -> np.array:
        return self.__predicted_labels

    @property
    def predicted_boxes(self) -> np.array:
        return self.__predicted_boxes

    @property
    def predicted_labels(self) -> np.array:
        return self.__predicted_labels
