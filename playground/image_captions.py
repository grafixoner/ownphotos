import requests
import base64

from django.core.files import File

from api.models import Photo

import ipdb
from io import StringIO

photos = Photo.objects.filter(deleted=False)

captions = []

for idx,photo in enumerate(photos):
    if idx > 2: break
    # try:
    thumbnail_path = photo.thumbnail.url
    with open("."+thumbnail_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    encoded_string = str(encoded_string)[2:-1]


    # ipdb.set_trace()
    resp_captions = requests.post('http://localhost:5000/',data=encoded_string)
    captions.append(resp_captions.json())

    # except Exception as e:
    #     print('error on image', photo.image_path)
    #     print(e.message)


