from src.commands import command_soon, command_subscribe, command_start, command_freegame #All commands of the bot are in the folder src.commands
from src.events import check_game #All events of the bot are in the folder src.events (ex. check_game = check when Epic Games change the game)
from bson.objectid import ObjectId #Library for MongoDB (read ObjectId)
from dotenv import load_dotenv #Library for .env file
from telebot import telebot #Libraries for Telegram bot
import os #Library for .env file (get env variables)
import urllib #Library for MongoDB (read password)
import pymongo #Library for MongoDB
import threading #Library for threading (ex. Check game every 10 seconds)

#Load all variables from .env file
load_dotenv() #Load .env file
API_TOKEN = os.getenv('BOT_TOKEN') #Token for Telegram bot
PASSWORD_MONGO = os.getenv('PASSWORD_MONGODB') #Password for MongoDB
URL_MONGO = os.getenv('URL_MONGODB') #URL for MongoDB

#Connect to MongoDB
mongo_url = "mongodb+srv://stefano:" + urllib.parse.quote_plus(PASSWORD_MONGO) + URL_MONGO #URL for MongoDB (with password)
client = pymongo.MongoClient(mongo_url) #Connect to MongoDB
database = client["epicgames-notifier"] #Database name
collection_id = database["id-user"] #Collection name (id-user)
collection_game = database["list-game"] #Collection name (list-game)

bot = telebot.TeleBot(API_TOKEN) #Connect to Telegram API

#Command /start
@bot.message_handler(commands=['start'])
def start(message, bot=bot):
    command_start.start_command(message, bot)

#Command /comingsoon
@bot.message_handler(commands=['comingsoon'])
def comingsoon(message, bot=bot):
    command_soon.soon_command(message, bot)

#Command /freenow
@bot.message_handler(commands=['freenow'])
def freegame_command(message, bot=bot):
    command_freegame.freegame_command(message, bot)

#Command /subscribe
@bot.message_handler(commands=['subscribe'])
def subscribe(message, bot=bot, collection_id=collection_id):
    command_subscribe.subscribe_command(message, bot, collection_id)

def event_game(collection_game=collection_game, collection_id=collection_id, bot=bot):
    check_game.a(collection_game, collection_id, bot)

#Threading for check game every 5 seconds
t1 = threading.Thread(target=event_game, args=())
t1.start()

bot.polling()
