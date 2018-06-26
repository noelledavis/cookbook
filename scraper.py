from requests import get        # read page from website
from bs4 import BeautifulSoup   # html parsing


url = 'https://smittenkitchen.com/2016/04/carrot-tahini-muffins/'
title = 'carrot tahini muffins'

response = get(url)
# print(response.text[:500])

html_soup = BeautifulSoup(response.text, 'lxml')
paragraph_text = html_soup.find_all('p')

print(paragraph_text)

for line in paragraph_text:
    if title in line.text.lower():
        print(line)