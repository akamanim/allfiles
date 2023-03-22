import requests
from bs4 import BeautifulSoup
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Обработчик команды /start
def start(update: Update, context: CallbackContext) -> None:
    # Получаем список новостей
    url = 'https://kaktus.media/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('a', class_='block')

    # Формируем сообщение с выбором новостей
    message = 'Выберите новость:\n\n'
    for i, article in enumerate(articles[:20]):
        message += f"{i+1}. {article.text}\n"
    message += '\nВведите номер новости:'

    # Отправляем сообщение
    update.message.reply_text(message)

    # Сохраняем список новостей в контексте
    context.user_data['articles'] = articles[:20]

# Обработчик кнопок выбора новости
def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    # Получаем выбранную новость
    article = context.user_data['articles'][int(query.data) - 1]

    # Получаем описание новости
    url = article['href']
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    description = soup.find('div', class_='text').text.strip()

    # Получаем картинку новости
    image_url = soup.find('div', class_='picture').find('img')['src']

    # Формируем сообщение с заголовком, описанием и картинкой
    message = f"{article.text}\n\n{description}"
    query.edit_message_text(text=message)
    query.message.reply_photo(photo=image_url)

# Обработчик команды /quit
def quit(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('До свидания!')

# Создаем и запускаем бота
def main() -> None:
    # Инициализация бота
    updater = Updater('6074708790:AAHkgqO7GVMwtuT-51g8zzeKHNR2BPGglEY')
    dispatcher = updater.dispatcher

    # Обработчики команд
    start_handler = CommandHandler('start', start)
    quit_handler = CommandHandler('quit', quit)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(quit_handler)

    # Обработчик кнопок
    dispatcher.add_handler(CallbackQueryHandler(button))

    # Запуск бота
    updater.start_polling()

    # Остановка бота при нажатии Ctrl+C
    updater.idle()

if __name__ == '__main__':
    main()