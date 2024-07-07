import requests
from bs4 import BeautifulSoup

with open('./nr.txt','r') as file:
    numbers = file.read().split('\n')

images = []
print(numbers)

def download_images(number):
    url = "https://xkcd.com/" + number + "/info.0.json"
    response = requests.get(url)
    data = response.json()
    return data['img']

for number in numbers:
    image = download_images(number)
    images.append(image)

with open('test.html','r') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content,'html.parser')

comics_list = soup.find('body')
for image_url in images:
    img = soup.new_tag('img',src=image_url)
    img['width'] = "100%"
    hr = soup.new_tag('hr')
    comics_list.append(img)
    comics_list.append(hr)

with open('index_modified.html', 'w') as file:
    file.write(soup.prettify())