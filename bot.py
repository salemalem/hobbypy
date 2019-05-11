import telebot
token = "761349437:AAFNrKXqTLYEsXs_ar9nNeeTZ1aUqMRmaNg"
chat_id = 184133103

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def handle_text(message):
    user_markup = telebot.types.ReplyKeyboardMarkup()
    user_markup.row('/start', '/stop')
    user_markup.row('баглан', 'аудио', 'документы')
    user_markup.row('стикер', 'голос', 'локация', 'видео')
    bot.send_message(message.from_user.id, 'Добро пожаловать', reply_markup=user_markup)

#user_markup = telebot.types.ReplyKeyboardHide()
bot.polling(none_stop=True, interval=3)