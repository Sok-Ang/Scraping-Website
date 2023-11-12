import httpx
from bs4 import BeautifulSoup
import numpy as np
from PIL import Image

url = "https://www.behance.net/gallery/178560893/Runholdy-Typeface"

response = httpx.get(url)

index = 0
image_links = []

soup = BeautifulSoup(response.text, 'html.parser')
for image_box in soup.select('div.ImageElement-root-kir'):
    index += 1
    result = {
        'link': image_box.select_one('img').attrs['src'],
        'title': str(index) + '.png'
    }
    image_links.append(result)

    if index == 16:
        break

for image_object in image_links:
    with open(f"./download_image/{image_object['title']}", 'wb') as file:
        image = httpx.get(image_object['link'])
        file.write(image.content)
        # print(f"Image {image_object['title']} has been scraped")

list_images = ['1.png', '2.png', '3.png', '4.png', '4.png', '5.png', '6.png', '7.png',
               '8.png','9.png','10.png','11.png','12.png','13.png', '14.png', '15.png','16.png']
images = [Image.open(f"./download_image/{image}") for image in list_images]

min_width, min_height = max((i.size for i in images))

images_resized = [i.resize((min_width, min_height)).convert('RGB') for i in images]

imgs_comb = np.vstack([np.array(i) for i in images_resized])

imgs_comb = Image.fromarray(imgs_comb)

imgs_comb.save("./download_image/vertical_image2.png")