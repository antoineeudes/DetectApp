import requests
from requests.exceptions import MissingSchema
from errors import FailedToDownloadException, EmptyStringException, InvalidURL
from PIL import Image, UnidentifiedImageError


def download_image(image_url):
    if len(image_url) == 0:
        raise EmptyStringException
    try:
        return Image.open(requests.get(image_url, stream=True).raw).convert("RGB")
    except UnidentifiedImageError:
        raise FailedToDownloadException
    except MissingSchema:
        raise InvalidURL
