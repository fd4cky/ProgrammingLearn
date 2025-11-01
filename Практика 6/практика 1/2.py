from PIL import Image
import requests
from io import BytesIO


def show_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()


def get_dogs():
    response = requests.get('https://dog.ceo/api/breeds/list/all').json()
    result = [breed for breed in response['message']]

    return result


def show_dogs(*breeds):
    for breed in breeds:
        response = requests.get(f'https://dog.ceo/api/breed/{breed}/images').json()
        url = response['message'][0]

        show_image(url)

print(get_dogs())
show_dogs('briard', 'pekinese')