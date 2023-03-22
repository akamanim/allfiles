''' ================ ~~~~~~~~~~~ parcing ~~~~~~~~~~~ ================== '''
# pip3 install -r dir -> Установка пакетов библиотек
# pip3 install name -> Установка только одной библиотеки
# pip freeze -> Проверить установленные библиотеки
# python3 -m venv venv создание виртуального окружения
# .venv/bin/activate -> активация виртуального окружения
''' ===================== ~~~~~~~~~~~~~~~~~~~~~~~ ===================== '''
import requests
from bs4 import BeautifulSoup
import csv

''' ===================== ~~~~~~~~~~~~~~~~~~~~~~~ ===================== '''
# Функция, для записи данных в директорию
def write_to_csv(data):
    with open('data.csv','a') as file:
        write = csv.writer(file)
        # write.writerow([data['title']])
        write.writerow([data['image']])
        # write.writerow([data['price']])
        # write.writerow([data['description']])
''' ===================== ~~~~~~~~~~~~~~~~~~~~~~~ ===================== '''
# Функция, для получения HTML
def get_html(url):
    responce = requests.get(url)
    return responce.text
''' ===================== ~~~~~~~~~~~~~~~~~~~~~~~ ===================== '''
# Функция, для получения конкретных DIV или других элементов, как в этом примере, мы импортировали фото и описание ноутбука
def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    products = soup.find('div',class_='list-view').find_all('div',class_='item product_listbox oh')
    # return product
    for prudict in products:
        title = prudict.find('div',class_='listbox_title').find('strong').text
        image = 'https://www.kivano.kg/'+prudict.find('img').get('src')
        price = prudict.find('div',class_='listbox_price').find('strong').text
        description = prudict.find('div', class_= 'product_text pull-left').text
        dict_= {'title':title,'image': image,'price':price,'description':description}
            # print(dict_)
        # write_to_csv(dict_)

''' ===================== ~~~~~~~~~~~~~~~~~~~~~~~ ===================== '''
def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    page_list = soup.find('div',class_='pager-wrap').find('ul',class_='pagination').find_all('li')
    last_page = page_list[-1].text
    # print(last_page)
    return int(last_page)
''' ===================== ~~~~~~~~~~~~~~~~~~~~~~~ ===================== '''

# Функция для загаловка, и что бы информация не дублировалась, а перезаписывалась!
with open('data.csv', 'w') as file:
    write = csv.writer(file)
    write.writerow(['title','image'])
''' ===================== ~~~~~~~~~~~~~~~~~~~~~~~ ===================== '''

# Функция для вызова всех функций
def main():
    url = 'https://www.kivano.kg/noutbuki'
    pages = '?page='
    html = get_html(url)
    number = get_total_pages(html)
    get_data(html)
    for i in range (2, number+1):
        url_with_page = url + pages + str(i)
        # print(url_with_page)
        html = get_html(url_with_page)
        get_data(html)
# main()
''' ===================== ~~~~~~~~~~~~ ДЗ ~~~~~~~~~~~ ===================== '''
''' Получить прайс и описание ноутбука'''
# get_total_pages(get_html('https://www.kivano.kg/noutbuki'))




def get_data():
    next_link = 2
    url = 'https://cars.kg/service/' + str(next_link)
    responce = requests.get(url) 
    soup = BeautifulSoup(responce.text, 'lxml')
    pruducts = soup.find('div',class_ = 'catalog-list').find_all('a', class_ = 'catalog-list-item')
    for i in pruducts:
        for product in pruducts: 
            try:
                image = product.find('img', class_ = 'catalog-item-cover-img').get('src')
            except:
                image = ''
        # print(image)
            print(image)
            dict_={"image":image}
            write_to_csv(dict_)
            print (next_link)
        next_link+=1


get_data()


