import os
import telebot

from ai import *
from config import BOT_TOKEN #custom info

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(msg):
    content = 'Hi, ' + msg.from_user.first_name + ", this is just a test bot and was\
 made just for programming practice but you still can use it for fun or\
 something. \nEnter /help to get list of commands."
    bot.send_message(msg.chat.id, content, parse_mode=None)

@bot.message_handler(content_types=['photo'])
def image_handle(msg):
    fileID = msg.photo[-1].file_id   
    file_info = bot.get_file(fileID)
    downloaded_file = bot.download_file(file_info.file_path)
    image_info = get_image_info(downloaded_file)
    bot.send_message(msg.chat.id, image_info, parse_mode=None)

@bot.message_handler()
def text_handle(msg):
    if msg.text == "joke":
        bot.send_message(msg.chat.id, get_joke(), parse_mode=None)
    elif msg.text == "photo":
        get_image()
        photo = open('img.jpg', 'rb')
        bot.send_photo(msg.chat.id, photo)
    else:
        bot.send_message(msg.chat.id, 'Unknown command! Enter /help to get command list.', parse_mode=None)

def start_bot():
    bot.polling(non_stop=True)
