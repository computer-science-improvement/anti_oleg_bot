import telebot
from googletrans import Translator

TOKEN = ''

bot = telebot.TeleBot(TOKEN, parse_mode=None)
t = Translator(raise_exception=True)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    a = t.detect(message.text)
    if "🤡" in message.text:
        bot.reply_to(message, "🤡")
    elif a.lang == 'ru':
        bot.reply_to(message, "🤡")


bot.infinity_polling()
