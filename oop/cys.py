import requests
from bs4 import BeautifulSoup as BS
import csv
"""
1)	В текстовом файле посчитать количество строк, а также для каждой отдельной строки определить количество в ней символов и слов.
"""
with open('req.txt', 'r') as file:
    bota = file.readlines()  
    lines = 0
    symbols = 0
    for bot in bota:
        lines += 1
        for bu in bot:
            symbols += 1

    print (lines,symbols,bota)

"""
2)	Спарсить vesti.kg только названия новостей(title) и записать результат в csv файл
"""
# url = 'https://vesti.kg/'
# def get_html(url):
#     responce = requests.get(url).text
#     return responce
# # print(get_html(url))
# def get_data(html):
#     soup = BS(html, 'lxml')
#     titles = soup.find('div', class_='gkInnerInsetLeft').find_all('div',class_='itemContainer itemContainerLast')
#     for title in titles:
#         news = title.find('h2').text
#         dict = {'news':news}
#         with open('title.csv', 'a') as data:
#             write = csv.writer(data)
#             write.writerow([dict['news']])

# with open('title.csv', 'w') as file:
#     book = csv.writer(file)
#     write = 'Title of Title'

# get_data(get_html(url))