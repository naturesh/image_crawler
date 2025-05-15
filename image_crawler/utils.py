import requests
import base64
from PIL import Image, ImageFile
from io import BytesIO

from .type import urlType, base64Type

def urlToBase64(url: urlType) -> base64Type:
    try:
        res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        return base64.b64encode(res.content).decode('utf-8')
    except Exception as e:
        print('failed: convert url to base64')


def base64ToImage(base64_image: base64Type) -> ImageFile:
    if ',' in base64_image: 
        base64_image = base64_image.split(',')[1]
    return Image.open(BytesIO(base64.b64decode(base64_image)))
