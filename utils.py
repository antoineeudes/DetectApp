import requests
from requests.exceptions import MissingSchema
from errors import FailedToDownloadException, EmptyStringException, InvalidURL
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.applications.imagenet_utils import decode_predictions
import numpy as np
import tensorflow as tf
from PIL import Image, UnidentifiedImageError


model = EfficientNetB0(weights="imagenet")
INPUT_SHAPE = (224, 224)


def download_image(image_url):
    if len(image_url) == 0:
        raise EmptyStringException
    try:
        return Image.open(requests.get(image_url, stream=True).raw).convert("RGB")
    except UnidentifiedImageError:
        raise FailedToDownloadException
    except MissingSchema:
        raise InvalidURL


def preprocess_image(img):
    image_copy = img.copy()
    image_copy = np.expand_dims(image_copy, axis=0)
    image_copy = tf.image.resize_with_pad(
        image_copy,
        *INPUT_SHAPE,
        method=tf.image.ResizeMethod.NEAREST_NEIGHBOR,  # keep tf.uint8 tensor
    )
    return image_copy


def predict_label(img):
    preprocessed_image = tf.Variable(preprocess_image(img))
    predictions = model(preprocessed_image).numpy()
    label = decode_predictions(predictions, top=1)
    return label[0][0]
