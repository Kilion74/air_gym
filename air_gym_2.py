import requests  # pip install requests
from bs4 import BeautifulSoup  # pip install bs4
import csv

# pip install lxml
print('Введите одну из следующих категорий: батуты для дачи, шведские стенки, детские шведские стенки, спортивные тренажёры')
category = input().lower()
telly = ''
if category == 'батуты для дачи':
    telly = 'batuty'
elif category == 'шведские стенки':
    telly = 'shvedskie-stenki'
elif category == 'детские шведские стенки':
    telly = 'detskie-shvedskie-stenki'
elif category == 'спортивные тренажёры':
    telly = 'trenazhery'
else:
    print('Введите корректные данные')

print('Введите название файла на английском')
filename = input().lower()
count = 0
while count <= 20:
    url = f'https://air-gym.ru/{telly}/page-{count}/?sort_by=position&sort_order=desc&layout=products_without_options'
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
        ssylka = i.find_next('div', class_='ut2-pl__item-name').find('a').get('href')
        print(ssylka)
        zagol = (name.text.strip())
        cena = i.find_next('span', class_='ty-price')
        print(cena.text.strip())
        price = (cena.text.strip())
        codd = i.find_next('span', class_='ty-control-group__item')
        print(codd.text.strip())
        get_code = (codd.text.strip())
        opiss = i.find_next('div', class_='ut2-pl__description')
        print(opiss.text.strip())
        tema = (opiss.text.strip())
        params = i.find_next('div', class_='ut2-pl__feature').find_all('span', class_='ty-control-group')
        # print(params[0].find_next('span', class_='ty-product-feature__label').text.strip())
        try:
            param_1 = (params[0].find_next('span', class_='ty-product-feature__label').text.strip())
            # print(params[0].find_next('span', class_='ty-product-feature__label').find_next('span').text.strip())
            value_1 = (params[0].find_next('span', class_='ty-product-feature__label').find_next('span').text.strip())
            print(param_1 + ':' + ' ' + value_1)
            charact_1 = (param_1 + ':' + ' ' + value_1)
        except:
            print('None')
            charact_1 = 'None'
        try:
            # print(params[0].find_next('span', class_='ty-product-feature__label').text.strip())
            param_2 = (params[1].find_next('span', class_='ty-product-feature__label').text.strip())
            # print(params[0].find_next('span', class_='ty-product-feature__label').find_next('span').text.strip())
            value_2 = (params[1].find_next('span', class_='ty-product-feature__label').find_next('span').text.strip())
            print(param_2 + ':' + ' ' + value_2)
            charact_2 = (param_2 + ':' + ' ' + value_2)
        except:
            print('None')
            charact_2 = 'None'
        try:
            # print(params[0].find_next('span', class_='ty-product-feature__label').text.strip())
            param_3 = (params[2].find_next('span', class_='ty-product-feature__label').text.strip())
            # print(params[0].find_next('span', class_='ty-product-feature__label').find_next('span').text.strip())
            value_3 = (params[2].find_next('span', class_='ty-product-feature__label').find_next('span').text.strip())
            print(param_3 + ':' + ' ' + value_3)
            charact_3 = (param_3 + ':' + ' ' + value_3)
        except:
            print('None')
            charact_3 = 'None'
        try:
            # print(params[0].find_next('span', class_='ty-product-feature__label').text.strip())
            param_4 = (params[3].find_next('span', class_='ty-product-feature__label').text.strip())
            # print(params[0].find_next('span', class_='ty-product-feature__label').find_next('span').text.strip())
            value_4 = (params[3].find_next('span', class_='ty-product-feature__label').find_next('span').text.strip())
            print(param_4 + ':' + ' ' + value_4)
            charact_4 = (param_4 + ':' + ' ' + value_4)
        except:
            print('None')
            charact_4 = 'None'
        try:
            # print(params[0].find_next('span', class_='ty-product-feature__label').text.strip())
            param_5 = (params[4].find_next('span', class_='ty-product-feature__label').text.strip())
            # print(params[0].find_next('span', class_='ty-product-feature__label').find_next('span').text.strip())
            value_5 = (params[4].find_next('span', class_='ty-product-feature__label').find_next('span').text.strip())
            print(param_5 + ':' + ' ' + value_5)
            charact_5 = (param_5 + ':' + ' ' + value_5)
        except:
            print('None')
            charact_5 = 'None'
        print('\n')

        storage = {'name': zagol, 'cena': price, 'code': get_code, 'param_1': charact_1,
                   'param_2': charact_2, 'param_3': charact_3, 'param_4': charact_4, 'param_5': charact_5,
                   'photo': photo, 'ssylka': ssylka}
        fields = ['Name', 'Price', 'Code', 'Param_1', 'Param_2', 'Param_3', 'Param_4', 'Param_5', 'Photo', 'URL']
        with open(f'{filename}.csv', 'a+', encoding='utf-16') as f:
            pisar = csv.writer(f, delimiter=';', lineterminator='\r')
            # Проверяем, находится ли файл в начале и пуст ли
            f.seek(0)
            if len(f.read()) == 0:
                pisar.writerow(fields)  # Записываем заголовки, только если файл пуст

            pisar.writerow([storage['name'], storage['cena'], storage['code'], storage['param_1'],
                            storage['param_2'], storage['param_3'], storage['param_4'], storage['param_5'],
                            storage['photo'], storage['ssylka']])
    count += 1
