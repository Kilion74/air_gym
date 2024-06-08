import requests  # pip install requests
from bs4 import BeautifulSoup  # pip install bs4

# pip install lxml


url = 'https://shvedstenki.ru/dlya-detey/page-2/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
data = requests.get(url, headers=headers).text
block = BeautifulSoup(data, 'lxml')
# print(block)
heads = block.find_all('div', class_='ty-column4')
print(len(heads))
for i in heads:
    w = i.find_next('div', class_='ut2-gl__name').find('a').get('href')
    # print(w)
    less = requests.get(w, headers=headers).text
    toom = BeautifulSoup(less, 'lxml')
    name = toom.find('h1', class_='ut2-pb__title')
    print(name.text.strip())
    cena = toom.find('div', class_='ut2-pb__price-actual')
    print(cena.text.strip())
    codd = toom.find('div', class_='ty-control-group ty-sku-item cm-hidden-wrapper')
    print(codd.text.strip())
    print('\n')
