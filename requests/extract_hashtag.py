from bs4 import BeautifulSoup
from selenium import webdriver
from urllib import parse

import time

keyword = input()

url = "https://www.instagram.com/explore/tags/{}/".format(keyword)


options = webdriver.ChromeOptions()

options.add_argument('headless')
options.add_argument('disable-gpu')
options.add_argument('lang=ko_KR')

driver = webdriver.Chrome('chromedriver', options=options)


driver.get(url)
time.sleep(3)

posts = []
images = driver.find_elements_by_css_selector('.Nnq7C img')

for img in images:
    post = img.get_attribute('src')
    posts.append(post)

for n in range(9, 21):
    posts[n-9] = posts[n]

print(posts)

driver.close()
