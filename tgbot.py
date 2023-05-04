import telebot
token='6067941673:AAGb2tDYIXexHvBIAsrkzFT0uOP6T8LcdS4'
bot = telebot.TeleBot(token)
@bot.message_handler(content_types=['text'])
def get_message(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Привет, это ты?")
    elif message.text.lower() == "да":
        bot.send_message(message.from_user.id, "пизда")
    elif message.text.lower() == "нет":
        bot.send_message(message.from_user.id, "пидора ответ")
    else:
        bot.send_message(message.from_user.id, "соси лалка")
bot.infinity_polling()
