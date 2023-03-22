import requests
from bs4 import BeautifulSoup
import csv
def write_to_csv(data):
    with open('data.csv','a') as file:
        write = csv.writer(file)
        write.writerow([data['title'], data['image']])
def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    page_list = soup.find('div',class_='pager-wrap').find('ul',class_='pagination').find_all('li')
    last_page = page_list[-1].text
    # print(last_page)
    return int(last_page)     
def get_html(url):
    response = requests.get(url)
    return response.text
def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    cars = soup.find('div',class_ = 'catalog-list').find_all('a', class_ = 'catalog-list-item')
    # print(cars)

    for car in cars:
        try:
            title = car.find('span', class_ = 'catalog-item-caption').text.strip()
        except:
            title = ''
        # print(title)
        try:
            image = car.find('img', class_ = 'catalog-item-cover-img').get('src')
        except:
            image = ''
        # print(image)
        data = {'title':title, 'image':image}
        
        write_to_csv(data)
with open('data.csv', 'w') as file:
    write = csv.writer(file)
    write = ('title','image')
def get_last_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    page_list = soup.find('div',class_='pages fl').find_all('a')
    last_page = page_list[-2].text
    # print(last_page)
    return int(last_page)
def main():
    url = 'https://cars.kg/offers'
    html = get_html(url)
    number = int(get_last_pages(html))
    # get_data(html)
    i = 1
    while i <= number:
        print(i)
        url  = f'https://cars.kg/offers/{i}'
        html = get_html(url)
        number = int(get_last_pages(html))
        i+=1
        if not BeautifulSoup(html, 'lxml').find('div', class_= 'catalog-list'):
            break
        # get_data(html)

main()
