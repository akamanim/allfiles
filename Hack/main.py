import telebot
token = '6074708790:AAHkgqO7GVMwtuT-51g8zzeKHNR2BPGglEY'
bot = telebot.TeleBot(token)

'''==============~~~~~~~~~~~~~~ FUNCTION ~~~~~~~~~~~~~~~==============='''
# @bot.message_handler(commands=['start','hi','aka','money'])#Обьявляем команды которые будем отправлять
# def start_messege(messege):#Команда которая будет приходить боту
#     bot.send_message(messege.chat.id,'Здарова,зайпал') # То, чем бот будет отвечать, вначале говорим, куда отправить
#     bot.send_sticker(messege.chat.id,'CAACAgIAAxkBAAEID-RkCd-5-fiQdtsc-nQ6PFZzd49SpwACSgkAAnlc4glshq449fyDqC8E')
keyboard = telebot.types.ReplyKeyboardMarkup()
baton1 = telebot.types.KeyboardButton('Смело')
baton2 = telebot.types.KeyboardButton('Не')
keyboard.add(baton1,baton2)

@bot.message_handler(commands='start')
def start_message(message):
    answer = bot.send_message(message.chat.id,'Игра?', reply_markup=keyboard)
    bot.register_next_step_handler(answer, check_answer)
def check_answer(answer):
    if answer.text =='Смело':
        bot.send_message(answer.chat.id, 'Поехали!')
        import random
        number = random.choice(range(1,5))
        print(number)
        game(answer,3,number)
def game(message,attempts,number):
    answer = bot.send_message(message.chat.id, 'Введите число')
    bot.register_next_step_handler(answer,check_number,attempts-1,number)
def check_number(answer,attempts,number):
    if answer.text == str(number):
        bot.send_message(answer.chat.id, 'Правилный ответ!')
    elif attempts == 0:
        bot.send_message(answer.chat.id, 'Попыток больше нема!')
    else:
        bot.send_message(answer.chat.id, 'Попробуйте, еще разок')
        game(answer,attempts,number)
bot.polling()