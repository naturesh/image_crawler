from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time, bs4

from .utils import urlToBase64, base64ToImage
from .type import base64Type





def get_image(query, geckodriver_path, scroll=10) -> list[base64Type]:

    # new instance
    service = Service(executable_path=geckodriver_path)
    options = Options()
    options.add_argument('-headless')
    firefox = webdriver.Firefox(service=service, options=options)
    firefox.set_window_size(1200, 1000)

    # request get 
    firefox.get(f'https://www.google.com/search?q={query}&source=hp&sclient=img&udm=2')


    # load images
    for _ in range(scroll): 
        firefox.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    
        time.sleep(0.5)
    
    # parse
    soup = bs4.BeautifulSoup(firefox.page_source, 'html.parser')
    image_element = soup.find_all(lambda tag: tag.has_attr('class') and tag.get('class') == ['YQ4gaf'])


    base64_images = []

    for src in map(lambda element: element.get('src'), image_element):
        if src.startswith('data:image'):base64_images.append(src)
        elif src: 
            base = urlToBase64(src)
            if base: base64_images.append(base)

    
    base64_images_ = []

    for b64 in base64_images:

        
        if ',' in b64: 
            b64 = b64.split(',')[1]

        if b64 == 'R0lGODlhAQABAIAAAP///////yH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==': continue
        base64_images_.append(b64)

        

    return base64_images_




# print(len(get_image('페페', '/Users/yangtaehwan/Desktop/finder/geckodriver',scroll=10)))

