#Libraries for Telegram bot
import telebot
from telebot import types, telebot
#Libraries for logging on console
import logging
#Libraries for get BOT_TOKEN
import os
#Boh
from dotenv import load_dotenv
#Libraries for use API
import requests
#Libraries for send message at a certain moment
import schedule
#Libraries for connect to Mongodb
import urllib
#Libraries for connect to Mongodb
import pymongo
#Libraries for search collection by Id
from bson.objectid import ObjectId
#Libraries for research game on db
import time

load_dotenv()
API_TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(API_TOKEN)

mongo_url = "mongodb+srv://stefano:" + urllib.parse.quote_plus("") + ""
client = pymongo.MongoClient(mongo_url)
database = client[""]
collection = database[""]

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

    image_futuregames2 = response['nextGames'][1]['keyImages'][1]['url'] # Second image future games
    future_games2 = response['nextGames'][1]['title'] # Second title future games
    future_games_description2 = response['nextGames'][1]['description'] # Second description future games
    future_games_startdate2 = response['nextGames'][1]['promotions']['upcomingPromotionalOffers'][0]['promotionalOffers'][0]['startDate']
    future_games_price2 = response['nextGames'][1]['price']['totalPrice']['fmtPrice']['originalPrice']

    try:
        image_futuregames3 = response['nextGames'][0]['keyImages'][2]['url'] # Third image future games
        future_games3 = response['nextGames'][2]['title'] # Third title future games
        future_games_description3 = response['nextGames'][2]['description'] # Third description future games
        future_games_startdate3 = response['nextGames'][1]['promotions']['upcomingPromotionalOffers'][0]['promotionalOffers'][0]['startDate']
        future_games_price3 = response['nextGames'][1]['price']['totalPrice']['fmtPrice']['originalPrice']
        title_description_3 = future_games3 + "\n\n<b>About:</b>\n" + future_games_description3 + "\n" + "\n<b>Start Date:</b>\n" + future_games_startdate3 + "\n" + "\n<b>Price:</b>\n" + future_games_price3 + " → " + "Free" # Send title, description, start date and price second future game
        img_3 = bot.send_photo(message.chat.id, image_futuregames3) # Send image third future games
        send_message = bot.send_message(chat_id, title_description_2, parse_mode="HTML") # Send all
    except IndexError:
        print("No third game")

    #Send notification to user
    title_description_1 = future_games1 + "\n\n<b>About:</b>\n" + future_games_description1 + "\n" + "\n<b>Start Date:</b>\n" + future_games_startdate1 + "\n" + "\n<b>Price:</b>\n" + future_games_price1 + " → " + "Free" # Send title, description, start date and price first future game
    img_1 = bot.send_photo(message.chat.id, image_futuregames1) # Send image first future games
    send_message = bot.send_message(chat_id, title_description_1, parse_mode="HTML") # Send all

    title_description_2 = future_games2 + "\n\n<b>About:</b>\n" + future_games_description2 + "\n" + "\n<b>Start Date:</b>\n" + future_games_startdate2 + "\n" + "\n<b>Price:</b>\n" + future_games_price2 + " → " + "Free" # Send title, description, start date and price second future game
    img_2 = bot.send_photo(message.chat.id, image_futuregames2) # Send image second future games
    send_message = bot.send_message(chat_id, title_description_2, parse_mode="HTML") # Send all

#Command /freenow
@bot.message_handler(commands=['freenow'])
def freenow(message):
    chat_id = message.chat.id
    url = "https://api.plenusbot.xyz/epic_games?country=IT"
    response = requests.get(url).json()
    image_currentgames1 = response['currentGames'][0]['keyImages'][0]['url'] # First image current games
    current_games1 = response['currentGames'][0]['title'] # First title current games
    current_games_description1 = response['currentGames'][0]['description'] # First description current games
    current_games_startdate1 = response['currentGames'][0]['promotions']['promotionalOffers'][0]['promotionalOffers'][0]['startDate']
    current_games_endate1 = response['currentGames'][0]['promotions']['promotionalOffers'][0]['promotionalOffers'][0]['endDate']
    current_games_price1 = response['currentGames'][0]['price']['totalPrice']['fmtPrice']['originalPrice']
    
    image_currentgames2 = response['currentGames'][1]['keyImages'][0]['url'] # First image current games
    current_games2 = response['currentGames'][1]['title'] # First title current games
    current_games_description2 = response['currentGames'][1]['description'] # First description current games
    current_games_startdate2 = response['currentGames'][1]['promotions']['promotionalOffers'][0]['promotionalOffers'][0]['startDate']
    current_games_endate2 = response['currentGames'][1]['promotions']['promotionalOffers'][0]['promotionalOffers'][0]['endDate']
    current_games_price2 = response['currentGames'][1]['price']['totalPrice']['fmtPrice']['originalPrice']

    #Send notification to user
    title_description_1 = current_games1 + "\n\n<b>About:</b>\n" + current_games_description1 + "\n" + "\n<b>Start Date:</b>\n" + current_games_startdate1 + "\n" + "\n<b>End Date:</b>\n" + current_games_endate1 + "\n" + "\n<b>Price:</b>\n" + current_games_price1 + " → " + "Free" # Send title, description, start date and price first current game
    img_1 = bot.send_photo(message.chat.id, image_currentgames1) # Send image first current games
    send_message = bot.send_message(chat_id, title_description_1, parse_mode="HTML") # Send all

    title_description_2 = current_games2 + "\n\n<b>About:</b>\n" + current_games_description2 + "\n" + "\n<b>Start Date:</b>\n" + current_games_startdate2 + "\n" + "\n<b>End Date:</b>\n" + current_games_endate2 + "\n" + "\n<b>Price:</b>\n" + current_games_price2 + " → " + "Free" # Send title, description, start date and price second current game
    img_2 = bot.send_photo(message.chat.id, image_currentgames2) # Send image second current games
    send_message = bot.send_message(chat_id, title_description_2, parse_mode="HTML") # Send all    

    try:
        image_currentgames3 = response['currentGames'][2]['keyImages'][0]['url'] # First image current games
        current_games3 = response['currentGames'][2]['title'] # First title current games
        current_games_description3 = response['currentGames'][2]['description'] # First description current games
        current_games_startdate3 = response['currentGames'][2]['promotions']['promotionalOffers'][0]['promotionalOffers'][0]['startDate']
        current_games_endate3 = response['currentGames'][2]['promotions']['promotionalOffers'][0]['promotionalOffers'][0]['endDate']
        current_games_price3 = response['currentGames'][2]['price']['totalPrice']['fmtPrice']['originalPrice']
        title_description_3 = current_games3 + "\n\n<b>About:</b>\n" + current_games_description3 + "\n" + "\n<b>Start Date:</b>\n" + current_games_startdate3 + "\n" + "\n<b>End Date:</b>\n" + current_games_endate3 + "\n" + "\n<b>Price:</b>\n" + current_games_price3 + " → " + "Free" # Send title, description, start date and price second current game
        img_3 = bot.send_photo(message.chat.id, image_currentgames3) # Send image second current games
        send_message = bot.send_message(chat_id, title_description_3, parse_mode="HTML") # Send all    
    except IndexError:
        print("No third game")

#Command /subscribe
@bot.message_handler(commands=['subscribe'])
def subscribe(message):
    #Register the user
    global chat_id
    chat_id = message.chat.id
    send_message = bot.send_message(chat_id, "✅ You have been successfully subscribed to Epic Games Store Free Games notifications!")
    #Get the ids of all users who write /subscribe
    take_id = message.from_user.id
    with open('readme.txt', 'a+') as f:
        f.write(str(take_id))
        f.writelines('\n')
        a()

def recheck_game():
    time.sleep(10)
    a()

#Function for send every week the notification
def a():
    #Read all id on readme.txt
    #schedule.every().thursday.do(freenow)
    schedule.every(10).seconds.do(freenow)
    
    #Check for new games
    url = "https://api.plenusbot.xyz/epic_games?country=IT"
    response = requests.get(url).json()

    # Title of current games
    current_games_title1 = response['currentGames'][0]['title']
    current_games_title2 = response['currentGames'][1]['title']

    #Check first game
    search_game1 = collection.find_one({"Game 1" : current_games_title1})
    if search_game1 is None:
        #Send notification if title game is changed
        print("There is a new game!")
        print("Now I'm sending the notification to everyone.")
        send_automatically1()
    else:
        #If new game is changed recheck every 10 second
        print("The game is not changed")
        recheck_game()


def send_automatically1():
    #Connect to the api
    url = "https://api.plenusbot.xyz/epic_games?country=IT"
    response = requests.get(url).json()

    #All information for first game
    current_games_title1 = response['currentGames'][0]['title'] # First title current games
    current_games_description1 = response['currentGames'][0]['description'] # First description current games
    current_games_startdate1 = response['currentGames'][0]['promotions']['promotionalOffers'][0]['promotionalOffers'][0]['startDate'] # Public release first game
    current_games_endate1 = response['currentGames'][0]['promotions']['promotionalOffers'][0]['promotionalOffers'][0]['endDate'] # End public release first game
    current_games_price1 = response['currentGames'][0]['price']['totalPrice']['fmtPrice']['originalPrice']
    current_games_images1 = response['currentGames'][0]['keyImages'][0]['url'] # First image current games

    #All information for second game
    current_games_title2 = response['currentGames'][1]['title'] # Second title current game
    current_games_images2 = response['currentGames'][1]['keyImages'][0]['url'] # Second image current game
    current_games_description2 = response['currentGames'][1]['description'] # Second description current game
    current_games_startdate2 = response['currentGames'][1]['promotions']['promotionalOffers'][0]['promotionalOffers'][0]['startDate'] #Public release second game
    current_games_endate2 = response['currentGames'][1]['promotions']['promotionalOffers'][0]['promotionalOffers'][0]['endDate'] # End public release second game
    current_games_price2 = response['currentGames'][1]['price']['totalPrice']['fmtPrice']['originalPrice'] # Original price second game

    with open('readme.txt', 'r') as f:
        for line in f:
            y = line.split()
            a = (', '.join(y))
            #Send first and second message when the free game title change
            title_description_1 = current_games_title1 + "\n\n<b>About:</b>\n" + current_games_description1 + "\n" + "\n<b>Start Date:</b>\n" + current_games_startdate1 + "\n" + "\n<b>End Date:</b>\n" + current_games_endate1 + "\n" + "\n<b>Price:</b>\n" + current_games_price1 + " → " + "Free" # Send title, description, start date and price first current game
            img_1 = bot.send_photo(a, current_games_images1) # Send image first current games
            send_message = bot.send_message(a, title_description_1, parse_mode="HTML") # Send all

    #Update Collection with new game
    send_game1 = {"Game 1": current_games_title1}
    senddata = collection.update_one({'_id':ObjectId("")}, {"$set": send_game1}, upsert=False)

    send_game2 = {"Game 2": current_games_title2}
    senddata = collection.update_one({'_id':ObjectId("")}, {"$set": send_game2}, upsert=False)

    recheck_game()

bot.polling()