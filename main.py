#Libraries for Telegram bot
import telebot
from telebot import types, telebot
#Libraries for logging on console
import logging
#
import os

from dotenv import load_dotenv
#Libraries for use API
import requests

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

#Command /comingsoon
@bot.message_handler(commands=['comingsoon'])
def comingsoon(message):
    chat_id = message.chat.id
    logging.info("Triggered command COMING SOON")
    url = "https://api.plenusbot.xyz/epic_games?country=IT"
    response = requests.get(url).json()
    # Title of future games
    image_futuregames1 = response['nextGames'][0]['keyImages'][0]['url'] # First image future games
    future_games1 = response['nextGames'][0]['title'] # First title future games
    future_games_description1 = response['nextGames'][0]['description'] # First description future games
    future_games_startdate1 = response['nextGames'][0]['promotions']['upcomingPromotionalOffers'][0]['promotionalOffers'][0]['startDate']
    future_games_price1 = response['nextGames'][0]['price']['totalPrice']['fmtPrice']['originalPrice']

    image_futuregames2 = response['nextGames'][0]['keyImages'][1]['url'] # Second image future games
    future_games2 = response['nextGames'][1]['title'] # Second title future games
    future_games_description2 = response['nextGames'][1]['description'] # Second description future games

    #image_futuregames3 = response['nextGames'][0]['keyImages'][2]['url'] # Third image future games
    #future_games3 = response['nextGames'][2]['title'] # Third title future games
    #future_games_description3 = response['nextGames'][2]['description'] # Third description future games

    title_description_1 = future_games1 + "\n\n<b>About:</b>\n" + future_games_description1 + "\n" + "\n<b>Start Date:</b>\n" + future_games_startdate1 + "\n" + "\n<b>Price:</b>\n" + future_games_price1 + " → " + "Free" # Send title, description, start date and price first future game
    img_1 = bot.send_photo(message.chat.id, image_futuregames1) # Send image first future games
    send_message = bot.send_message(chat_id, title_description_1, parse_mode="HTML") # Send all

bot.polling()