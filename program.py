# pobieranie liczb z pliku
# łączenie z serwerem
# # z pomocą api pobrać obrazki bądź linki
# generacja pliku html (uzyc bootstrap)
import requests

with open('./nr.txt','r') as file:
    numbers = file.read().split('\n')
images = []
print(numbers)

def download_images(number):
    url = "https://xkcd.com/" + number + "/info.0.json"
    response = requests.get(url)
    data = response.json()

    url_image = data['img']
    image = requests.get(url_image)
    return image

# for number in numbers:
#     image = download_images(number)
#     images.append(image)

#with open('index.html','w') as index:
