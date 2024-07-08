import requests
from bs4 import BeautifulSoup

with open('./nr.txt','r') as file:
    numbers = file.read().split('\n')

images = []
titles = []
print(numbers)

def download_images(number):
    url = "https://xkcd.com/" + number + "/info.0.json"
    response = requests.get(url)
    data = response.json()
    return data['img'], data['title']

for number in numbers:
    image, title = download_images(number)
    images.append(image)
    titles.append(title)

with open("./komiksy-kopia.html", 'r') as file:
    content = file.read()

soup = BeautifulSoup(content,'html.parser')

comics_list = soup.find('section')
for number, image_url, image_title in zip(numbers,images,titles):
    article = soup.new_tag('article',class_="my-3")
    div = soup.new_tag('div',class_="bd-heading sticky-xl-top align-self-start mt-5 mb-3 mt-xl-0 mb-xl-2")
    title = soup.new_tag('h3')
    title.string = number + ' : ' + image_title
    div2 = soup.new_tag('div')

    snippet = soup.new_tag('div',class_="bd-example-snippet bd-code-snippet")
    example = soup.new_tag('div',class_="bd-example m-0 border-0")

    img = soup.new_tag('img',src=image_url)
    img['width'] = "100%"
    img['height'] = "30%"

    hr = soup.new_tag('hr')

    example.append(img)
    example.append(hr)
    snippet.append(example)
    div2.append(snippet)
    div.append(title)
    article.append(div)
    article.append(div2)
    comics_list.append(article)

with open('comics.html', 'w') as file:
    file.write(soup.prettify())

print("Strona z wybranymi jest gotowa. Otworz plik comics.html w przegladarce.")
