import os
import telebot

from api import *
from config import BOT_TOKEN #custom info

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(msg):
    content = 'Hi, ' + msg.from_user.first_name + ", this is just a test bot and was\
 made for programming practice but you still can use it for fun or\
 something. \n\nEnter /help to get list of commands."
    bot.send_message(msg.chat.id, content, parse_mode=None)

@bot.message_handler(commands=['help'])
def help(msg):
    content = 'Enter these strings to get output:\n\n\
    1. [joke/dad joke] provides you with random joke \N{grinning face}\n\
    2. [word] provides you with random word \N{speech balloon}\n\
    3. [quote] provides you with random quote Ⓒ\n\
    4. [fact] provides you with random fact \N{check mark}\n\
    5. [photo] provides you with random image \N{sunrise}\n\n\
    You also can:\n\
    6. Send your own picture so the AI could detect objects on it \N{grapes}\n\
    7. Send any word to get it`s definition \N{open book}\n\
    8. Send anything to mood check yourself \N{turtle}'
    bot.send_message(msg.chat.id, content, parse_mode=None)

@bot.message_handler(content_types=['photo'])
def image_handle(msg):
    fileID = msg.photo[-1].file_id   
    file_info = bot.get_file(fileID)
    downloaded_file = bot.download_file(file_info.file_path)
    image_info = get_image_info(downloaded_file)
    if image_info == '':
        image_info = 'I can`t tell what is in the photo :('
    bot.send_message(msg.chat.id, image_info[:500], parse_mode=None)

@bot.message_handler()
def text_handle(msg):
    if msg.text == "joke" or msg.text == "Joke":
        bot.send_message(msg.chat.id, get_joke(), parse_mode=None)
    elif msg.text == "dad joke" or msg.text == "dad" or msg.text == "Dad joke":
        bot.send_message(msg.chat.id, get_dad_joke(), parse_mode=None)
    elif msg.text == "word" or msg.text == "rword" or msg.text == "Rword":
        bot.send_message(msg.chat.id, get_rword(), parse_mode=None)
    elif msg.text == "fact" or msg.text == "Fact":
        bot.send_message(msg.chat.id, get_fact(), parse_mode=None)
    elif msg.text == "quote" or msg.text == "Quote":
        bot.send_message(msg.chat.id, get_quote(), parse_mode=None)
    elif msg.text == "photo" or msg.text == "Photo":
        get_image()
        photo = open('img.jpg', 'rb')
        bot.send_photo(msg.chat.id, photo)
    else:
        if get_definition(msg.text) != None:
            bot.send_message(msg.chat.id, get_definition(msg.text)[:1000], parse_mode=None)
        else:
            bot.send_message(msg.chat.id, get_mood(msg.text), parse_mode=None)

def start_bot():
    bot.polling(non_stop=True)