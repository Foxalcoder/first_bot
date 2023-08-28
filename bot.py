import telebot
from telebot import types

from conf import tocken

API_TOKEN = ''

bot = telebot.TeleBot(tocken)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "hello")


@bot.message_handler(content_types=['audio', 'photo', 'voice', 'video', 'document', 'text', 'location', 'contact', 'sticker'])
def echo_message(message):
    match message.content_type:
        case "audio":
            pass
            # TODO: fix me
        case "photo":
            pass
            # TODO: fix me
        case "voice":
            pass
            # TODO: fix me
        case "video":
            pass
            # TODO: fix me
        case "document":
            pass
            # TODO: fix me
        case "text":
            bot.send_message(message.from_user.id, message.text)
        case "location":
            pass
            # TODO: fix me
        case "contact":
            pass
            # TODO: fix me
        case "sticker":
            pass
            # TODO: fix me

if __name__ == "__main__":
    bot.infinity_polling()