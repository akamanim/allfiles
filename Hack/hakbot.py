import requests
from bs4 import BeautifulSoup as BS
import csv
import telebot
from datetime import datetime
import json
today = datetime.today()

''' 
При нажатии на кнопку start, телеграмм бот должен
зайти на сайт KaktusMedia (https://kaktus.media/) и
спарсить категорию “Все новости”
2. При вводе текста должны выйти первые 20
заголовков статей с нумерацией. Должна быть
возможность выбрать новости по нумерации или id
(по желанию)
3. После выбора новости по нумерации, телеграмм
бот должен отправить сообщение в виде “some
title news you can see Description of this news
and Photo” и пользователь отправит текст (либо
нажмет кнопку) Description, то бот должен
отправить описание именно текущего поста, также
аналогично с Photo.
4. При нажатии на кнопку «Quit» бот должен
отправить сообщение “До свидания“

'''

def get_html(url):
    responce = requests.get(url)
    return responce.text
buta = ''
def get_data(html):
    soup = BS(html, 'lxml')
    contents = soup.find('div',class_= 'Tag').find_all('div',class_='Tag--article')
    number = 1
    try:    
        for content in contents:
            image = content.find('a',class_='ArticleItem--image').find('img').get('data-src')
            p = content.find('a',class_='ArticleItem--name').text
            news = f'{number}:  {p} - {image}\n'
            # global buta
            # buta += news
            # write_to_csv(news)
            number += 1
            if number >= 21:
                break
            with open('test.json', 'a') as file:
                file.write(news)
            # print(news)
    except:
            news = 'Не найдено!'
    return news



with open('test.json', 'w') as file:
    pass
def main():
    url = 'https://kaktus.media/?lable=8&date='
    date = today.date()
    order = '&order=time'
    html = get_html(url+str(date)+order)
    get_data(html)
main()

token = '6074708790:AAHkgqO7GVMwtuT-51g8zzeKHNR2BPGglEY'
bot = telebot.TeleBot(token)

keyboard = telebot.types.ReplyKeyboardMarkup()
baton1 = telebot.types.KeyboardButton('Отправить новости')
baton2 = telebot.types.KeyboardButton('ВЫйти')
keyboard.add(baton1,baton2)

with open('test.json') as file:
    buta = json.loads(file)
print(buta)
@bot.message_handler(commands='start')
def start_message(message):
    answer = bot.send_message(message.chat.id,'Желаете увидеть новости?', reply_markup=keyboard)
    bot.register_next_step_handler(answer, check_answer)
def check_answer(answer):
    if answer.text =='Отправить новости':
        bot.send_message(answer.chat.id, buta)
bot.polling()