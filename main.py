#Libraries for Telegram bot
import telebot
from telebot import types, telebot
#Libraries for logging on console
import logging
#
import os

from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(API_TOKEN)

logging.info("The bot started successfully.")

#Command /start
@bot.message_handler(commands=['start'])
def start_command(message):
    chat_id = message.chat.id
    logging.info("Triggered command START.")
    messageText = "✋ Welcome to <b>Epic Games Notifier</b>\n\n📱 You will be notified every week when there are new free games in the Epic Games Store. \n\n👨‍💻 Created and developed by @Stef58_Official"
    bot.send_message(chat_id, messageText, parse_mode="HTML")

bot.polling()