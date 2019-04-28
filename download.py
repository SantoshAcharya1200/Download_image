import requests
from bs4 import BeautifulSoup as bs
import os

# website with model images
url = 'https://stock.adobe.com/search?load_type=search&is_recent_search=&k=motivational&native_visual_search=&similar_content_id='

# download page for parsing
page = requests.get(url)
soup = bs(page.text, 'html.parser')

# locate all elements with image tag
image_tags = soup.findAll('img')

# create directory for model images
if not os.path.exists('quotes'):
    os.makedirs('quotes')

# move to new directory
os.chdir('quotes')

# image file name variable
x = 0

# writing images
for image in image_tags:
    try:
        url = image['src']
        response = requests.get(url)
        if response.status_code == 200:
            with open('quote-' + str(x) + '.jpg', 'wb') as f:
                f.write(requests.get(url).content)
                f.close()
                x += 1
    except:
        pass
