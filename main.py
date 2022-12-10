#Libraries for Telegram bot
from src.commands import soon_command, subscribe_command, start_command, command_freegame
from src.events import check_game
import telebot
from telebot import telebot
import os
import sys
import urllib
import pymongo
from bson.objectid import ObjectId
from dotenv import load_dotenv
import threading


load_dotenv()
API_TOKEN = os.getenv('BOT_TOKEN')
PASSWORD_MONGO = os.getenv('PASSWORD_MONGODB')
URL_MONGO = os.getenv('URL_MONGODB')
OBJECTID_game1 = os.getenv('OBJECTID_game1')
OBJECTID_game2 = os.getenv('OBJECTID_game2')
OBJECTID_idlist = os.getenv('OBJECTID_idlist')
bot = telebot.TeleBot(API_TOKEN)
mongo_url = "mongodb+srv://stefano:" + urllib.parse.quote_plus(PASSWORD_MONGO) + URL_MONGO
client = pymongo.MongoClient(mongo_url)
database = client["epicgames-notifier"]
collection_id = database["id-user"]
collection_game = database["list-game"]

#Command /start
@bot.message_handler(commands=['start'])
def start(message, bot=bot):
    start_command.start_command(message, bot)


#Command /comingsoon
@bot.message_handler(commands=['comingsoon'])
def comingsoon(message, bot=bot):
    soon_command.soon_command(message, bot)

#Command /freenow
@bot.message_handler(commands=['freenow'])
def freegame_command(message, bot=bot):
    command_freegame.freegame_command(message, bot)

#Command /subscribe
@bot.message_handler(commands=['subscribe'])
def subscribe(message, bot=bot, collection_game=collection_game):
    subscribe_command.subscribe_command(message, bot, collection_game)

def event_game(collection_game=collection_game, collection_id=collection_id, bot=bot, OBJECTID_idlist=OBJECTID_idlist, OBJECTID_game1=OBJECTID_game1, OBJECTID_game2=OBJECTID_game2):
    check_game.a(collection_game, collection_id, bot, OBJECTID_idlist, OBJECTID_game1, OBJECTID_game2)

t1 = threading.Thread(target=event_game, args=())
t1.start()

bot.polling()
