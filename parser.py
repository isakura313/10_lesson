from bs4 import BeautifulSoup
import requests
import os
import re

data = requests.get("https://www.combook.ru/")
data = data.text
soup = BeautifulSoup(data, 'html.parser')
# print(soup.prettify())
name_folder = input("введите название папки ")
os.mkdir(name_folder)

images = soup.find_all('img')
for i in range(len(images)):
    data = f'https://www.combook.ru/{images[i]["src"]}'
    print(data)
    data = requests.get(data)
    with open(f'{name_folder}/{str(i)}.jpg', 'wb') as f:
        f.write(data.content)


