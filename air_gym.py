import requests  # pip install requests
from bs4 import BeautifulSoup  # pip install bs4

# pip install lxml


url = 'https://air-gym.ru/detskie-shvedskie-stenki/page-2/?sort_by=position&sort_order=desc&layout=products_without_options'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
data = requests.get(url, headers=headers).text
block = BeautifulSoup(data, 'lxml')
# print(block)
heads = block.find_all('div', class_='ty-product-list clearfix')
print(len(heads))
for i in heads:
    photo = i.find('img').get('data-src')
    print(photo)
    name = i.find('div', class_='ut2-pl__item-name')
    print(name.text.strip())
    cena = i.find_next('span', class_='ty-price')
    print(cena.text.strip())
    codd = i.find_next('span', class_='ty-control-group__item')
    print(codd.text.strip())
    opiss = i.find_next('div', class_='ut2-pl__description')
    print(opiss.text.strip())
    params = i.find_next('div', class_='ut2-pl__feature').find_all('span', class_='ty-control-group')
    # print(params[0].find_next('span', class_='ty-product-feature__label').text.strip())
    param_1 = (params[0].find_next('span', class_='ty-product-feature__label').text.strip())
    # print(params[0].find_next('span', class_='ty-product-feature__label').find_next('span').text.strip())
    value_1 = (params[0].find_next('span', class_='ty-product-feature__label').find_next('span').text.strip())
    print(param_1 + ':' + ' ' +value_1)

    # print(params[0].find_next('span', class_='ty-product-feature__label').text.strip())
    param_2 = (params[1].find_next('span', class_='ty-product-feature__label').text.strip())
    # print(params[0].find_next('span', class_='ty-product-feature__label').find_next('span').text.strip())
    value_2 = (params[1].find_next('span', class_='ty-product-feature__label').find_next('span').text.strip())
    print(param_2 + ':' + ' ' + value_2)

    # print(params[0].find_next('span', class_='ty-product-feature__label').text.strip())
    param_3 = (params[2].find_next('span', class_='ty-product-feature__label').text.strip())
    # print(params[0].find_next('span', class_='ty-product-feature__label').find_next('span').text.strip())
    value_3 = (params[2].find_next('span', class_='ty-product-feature__label').find_next('span').text.strip())
    print(param_3 + ':' + ' ' + value_3)

    # print(params[0].find_next('span', class_='ty-product-feature__label').text.strip())
    param_4 = (params[3].find_next('span', class_='ty-product-feature__label').text.strip())
    # print(params[0].find_next('span', class_='ty-product-feature__label').find_next('span').text.strip())
    value_4 = (params[3].find_next('span', class_='ty-product-feature__label').find_next('span').text.strip())
    print(param_4 + ':' + ' ' + value_4)

    # print(params[0].find_next('span', class_='ty-product-feature__label').text.strip())
    param_5 = (params[4].find_next('span', class_='ty-product-feature__label').text.strip())
    # print(params[0].find_next('span', class_='ty-product-feature__label').find_next('span').text.strip())
    value_5 = (params[4].find_next('span', class_='ty-product-feature__label').find_next('span').text.strip())
    print(param_5 + ':' + ' ' + value_5)
    print('\n')
