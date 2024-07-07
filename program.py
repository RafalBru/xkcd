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

content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Comics</title>
    <style>
        body {
            text-align: center;
        }
        img {
            border-color: blue;
            border-width: 3px;
        }
    </style>
</head>
<body>

</body>
</html>
"""
#with open('test.html','r') as file:
 #   html_content = file.read()

soup = BeautifulSoup(content,'html.parser')

comics_list = soup.find('body')
for image_url in images:
    img = soup.new_tag('img',src=image_url)
    img['width'] = "500px"
    #img['height'] = "200px"
    
    hr = soup.new_tag('hr')
    comics_list.append(img)
    comics_list.append(hr)

with open('index.html', 'w') as file:
    file.write(soup.prettify())